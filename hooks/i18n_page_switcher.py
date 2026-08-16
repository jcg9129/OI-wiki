"""Make the header language switcher point at the current page's counterpart.

mkdocs-static-i18n already computes, for every page, the URL of its equivalent
in each build language (``page.file.alternates``). It normally writes those URLs
into ``config.extra.alternate`` so Material's selector links you to the *same*
page in the other language. That step is gated on ``theme.name == "material"``
(reconfigure.py), but OI Wiki uses the Material fork through ``custom_dir`` with
``theme.name: null``, so the gate never fires and the selector falls back to the
static per-language roots declared in ``mkdocs.yml``.

This hook reproduces just that missing step. It runs on ``on_page_context`` after
the plugin, and for each page rewrites the ``link`` of every ``extra.alternate``
entry to that page's counterpart when one exists, leaving the configured root
link as the fallback otherwise.
"""

from copy import deepcopy

# Pristine copy of the alternate list as configured in mkdocs.yml. Captured once
# because we overwrite config.extra.alternate per page and must rebuild from the
# original each time rather than from the previous page's (page-specific) links.
_original_alternate = None


def on_page_context(context, page, config, nav, **kwargs):
    global _original_alternate

    alternate = config.get("extra", {}).get("alternate")
    if not alternate:
        return context

    if _original_alternate is None:
        _original_alternate = deepcopy(alternate)

    # Rebuild from the pristine roots so a page without a given translation keeps
    # the language-root fallback instead of inheriting the last page's link.
    rebuilt = deepcopy(_original_alternate)

    alternates = getattr(page.file, "alternates", None) or {}
    for entry in rebuilt:
        counterpart = alternates.get(entry.get("lang"))
        if counterpart is not None:
            entry["link"] = counterpart.url

    config["extra"]["alternate"] = rebuilt
    return context
