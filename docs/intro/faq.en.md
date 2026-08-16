This page mainly answers some frequently asked questions.

## I want to ask something about this wiki

Q: Why did you decide to make this wiki?

A: When you were learning **OI**, did you ever feel lost and helpless in the face of such a vast body of knowledge? What **OI Wiki** wants to do is perhaps something like "making it easy for students with limited access to contest resources to reach training materials". Of course, that description isn't the whole story — the motivation for making the wiki may also be quite simple: we just wanted to make a tiny contribution to the development of **OI**. XD

***

Q: I'm interested — how can I take part?

A: **OI Wiki** is now hosted on GitHub. You can visit this [repo](https://github.com/OI-wiki/OI-wiki) directly to see the latest progress. Ways to participate include opening an [Issue](https://github.com/OI-wiki/OI-wiki/issues) or [Pull Request](https://github.com/OI-wiki/OI-wiki/pulls) on GitHub, sharing your ideas in the chat groups, or submitting content directly to the maintainers. The framework we currently use is [MkDocs](https://mkdocs.readthedocs.io), developed in Python, which supports the Markdown format (and also supports inserting mathematical formulas).

***

Q: But I'm rather weak… I'm not sure what I can do.

A: It all starts with passion. You can help others review and revise drafts, help us promote **OI Wiki**, and foster a good atmosphere for learning and exchange in the community!

***

Q: Who is mainly doing this now? It feels like a huge undertaking — can it really be done well?

A: At first it was mainly some retired veteran contestants doing this, and later we met many like-minded friends: active contestants, retired players, and even friends who have never taken part in **OI**. The project is currently maintained mainly by the **OI Wiki** team (here is a group photo).

<a href="https://github.com/OI-wiki/OI-wiki/graphs/contributors"><img src="https://opencollective.com/oi-wiki/contributors.svg?width=890&button=false"/></a>

Of course, it is hard to make this project perfect by our strength alone, and we sincerely invite you to help improve **OI Wiki** together.

***

Q: How do you guarantee that the content we add won't suddenly disappear?

A: We host the content on [GitHub](https://github.com/OI-wiki/OI-wiki), so even if our servers go down, the content won't be lost. In addition, we regularly back up everyone's hard work, so even if one day GitHub shuts down (?), our content won't be lost.

***

Q: It looks like **OI Wiki** has some empty pages!

A: Yes. Limited by the team members' expertise and time, we cannot finish these empty pages for the moment. So we are soliciting contributions and recruiting here, hoping to meet friends who share the same idea, so we can improve **OI Wiki** together.

***

Q: Why not just write for [Chinese Wikipedia](https://zh.wikipedia.org/)?

A: Because we hope to genuinely help more contestants or people interested in this content. Moreover, for reasons everyone knows, the content on Chinese Wikipedia is not accessible without barriers.

## I want to get involved!

Q: How do I communicate with the team?

A: You can contact us through the [contact methods in About This Project](./about.md#how-to-get-in-touch).

***

Q: How do I contribute code or content?

Please refer to the [How to Contribute](./htc.md) page.

***

Q: Where is the navigation?

A: The navigation is in the [mkdocs.yml](https://github.com/OI-wiki/OI-wiki/blob/master/mkdocs.yml#L17) file in the project's root directory.

***

Q: How do I modify the content of a topic?

A: There is an edit button <i class="md-icon">edit</i> at the top right of the corresponding page. Click it and, after confirming that you have read [How to Contribute](./htc.md), you will be redirected to the location of the corresponding file on GitHub.

Alternatively, you can read the navigation [(mkdocs.yml)](https://github.com/OI-wiki/OI-wiki/blob/master/mkdocs.yml) yourself to find the file location.

***

Q: How do I add a topic?

A: You have two options:

-   Open an Issue noting the content you'd like to add.
-   Open a Pull Request, add the new topic to the navigation [(mkdocs.yml)](https://github.com/OI-wiki/OI-wiki/blob/master/mkdocs.yml), and create an empty `.md` file at the corresponding location under the [docs](https://github.com/OI-wiki/OI-wiki/tree/master/docs) folder. For details on the document format, please refer to the [format manual](./format.md#贡献文档要求).

***

Q: I ran into trouble trying to access GitHub.

A: We recommend adding the following lines to your hosts file [^ref1]:

```text
# GitHub Start
140.82.114.25                 alive.github.com
140.82.113.5                  api.github.com
185.199.110.153               assets-cdn.github.com
185.199.111.133               avatars.githubusercontent.com
185.199.111.133               avatars0.githubusercontent.com
185.199.111.133               avatars1.githubusercontent.com
185.199.111.133               avatars2.githubusercontent.com
185.199.111.133               avatars3.githubusercontent.com
185.199.111.133               avatars4.githubusercontent.com
185.199.111.133               avatars5.githubusercontent.com
185.199.111.133               camo.githubusercontent.com
140.82.112.22                 central.github.com
185.199.111.133               cloud.githubusercontent.com
140.82.114.9                  codeload.github.com
140.82.113.22                 collector.github.com
185.199.111.133               desktop.githubusercontent.com
185.199.111.133               favicons.githubusercontent.com
140.82.112.3                  gist.github.com
52.216.163.147                github-cloud.s3.amazonaws.com
52.217.124.1                  github-com.s3.amazonaws.com
52.216.144.83                 github-production-release-asset-2e65be.s3.amazonaws.com
52.217.121.249                github-production-repository-file-5c1aeb.s3.amazonaws.com
52.217.206.57                 github-production-user-asset-6210df.s3.amazonaws.com
192.0.66.2                    github.blog
140.82.114.4                  github.com
140.82.113.18                 github.community
185.199.110.154               github.githubassets.com
151.101.1.194                 github.global.ssl.fastly.net
185.199.110.153               github.io
185.199.111.133               github.map.fastly.net
185.199.110.153               githubstatus.com
140.82.112.25                 live.github.com
185.199.111.133               media.githubusercontent.com
185.199.111.133               objects.githubusercontent.com
13.107.42.16                  pipelines.actions.githubusercontent.com
185.199.111.133               raw.githubusercontent.com
185.199.111.133               user-images.githubusercontent.com
13.107.253.40                 vscode.dev
140.82.112.21                 education.github.com
# GitHub End
```

You can find the latest content and more information at [GitHub520](https://gitee.com/klmahuaw/GitHub520).

Linux and macOS users can try [lilydjwg](https://github.com/lilydjwg/)'s [gh-check script](https://gist.github.com/lilydjwg/93d33ed04547e1b9f7a86b64ef2ed058) to obtain the fastest IP for access; the `--hosts` argument can update the hosts file directly, and `--help` gives usage help. You first need to install Python 3 and aiohttp (`pip install aiohttp -i https://pypi.tuna.tsinghua.edu.cn/simple/`). See lilydjwg's blog post for an introduction: [Finding the fastest GitHub IP](https://blog.lilydjwg.me/2019/8/16/gh-check.214730.html).

You can also use the [Gitclone](https://www.gitclone.com/) service to speed up cloning; see the instructions on its homepage.

If you just want to clone the **OI Wiki** repository:

```bash
git clone https://gitclone.com/github.com/OI-wiki/OI-wiki
```

If you need to contribute to **OI Wiki**, first fork the **OI Wiki** repository, then (replace `username` with your username). Note that the example provided will have you connect to GitHub over SSH [^only-ssh-connect]:

```bash
git clone https://gitclone.com/github.com/username/OI-wiki
git remote set-url origin git@github.com:username/OI-wiki.git
```

***

Q: pip is way too slow for me!

A: You can switch to a domestic mirror [^ref2], or:

```bash
pip install -U -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

***

Q: I cloned this project on my client, and it's too slow.

A: If you have `git bash` installed, you can add a few limits to reduce the download size. [^ref3]

```bash
git clone https://github.com/OI-wiki/OI-wiki.git --depth=1 -b master
```

***

Q: I've never installed Python 3.

A: You can visit the [Python official site](https://www.python.org/downloads/) for more information.

***

Q: It seems to tell me that my pip version is too low.

A: After entering cmd/shell, run the following command:

```bash
python -m pip install --upgrade pip
```

***

Q: I failed to install the dependencies.

A: Check: network? permissions? Look at the error message?

***

Q: I've cloned it, so why can't I deploy it?

A: Check whether the dependencies are installed properly?

***

Q: I cloned the repo a long time ago — how do I update to the new version?

A: Please refer to GitHub's official help page, [Syncing a fork - GitHub Docs](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork).

***

Q: How do I update if I installed the old dependencies?

A: Please run the following command:

```bash
pip install -U -r requirements.txt
```

***

Q: Why is my Markdown formatting messed up?

A: You can consult [cyent's notes](https://web.archive.org/web/20221103014610/https://cyent.github.io/markdown-with-mkdocs-material/), or the [MkDocs usage guide](https://github.com/ctf-wiki/ctf-wiki/wiki/Mkdocs-%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E).

We currently use [remark-lint](https://github.com/remarkjs/remark-lint) to automatically fix formatting; there may still be some [configuration](https://github.com/OI-wiki/OI-wiki/blob/master/.remarkrc) that isn't good enough — you are welcome to point it out.

***

Q: Doesn't GitHub display my math formulas?

A: That's right — GitHub's preview does not display math formulas. But rest assured, MkDocs supports math formulas and works fine; any syntax supported by MathJax can be used.

***

Q: Why are my math formulas garbled?

A: For display formulas (using `$$`), a known issue is that you need to leave blank lines on both sides of the `$$`, and the `$$` must be placed **alone** on its own line (with no leading space). The format is as follows:

```text
// blank line
$$
a_i
$$
// blank line
```

***

Q: Why doesn't my formula display correctly in the table of contents? It seems doubled.

A: Yes, this is a bug in python-markdown that may be fixed soon.

To avoid doubled formulas in the table of contents, you can refer to [the way the SAM entry under the string category writes its headings](https://github.com/OI-wiki/OI-wiki/blame/master/docs/string/sam.md#L73).

```text
结束位置 <script type="math/tex">endpos</script>
```

becomes, in the table of contents,

```text
结束位置 endpos
```

Note: for now, please avoid introducing MathJax formulas in the table of contents.

***

Q: How do I declare copyright information for a single page?

A: Just add a line at the beginning of the page. [^ref4]

For example:

```text
copyright: SATA
```

Note: the default is CC BY-SA 4.0 and SATA.

***

Q: Why isn't my name in the author statistics?

A: If you find that you wrote part of the content on a page but were not recorded in the author list, you can add your GitHub ID to the [author field](./htc.md#the-author-field) in the file header.

***

Thank you for reading to the end. What we urgently need right now is your help.

The **OI Wiki** team

2018.8

## References and Notes

[^ref1]: [GitHub520](https://gitee.com/klmahuaw/GitHub520)

[^ref2]: [Changing the pip source to a domestic mirror - L瑜 - CSDN Blog](https://blog.csdn.net/lambert310/article/details/52412059)

[^ref3]: [GIT — Step-by-step getting started (Windows Git Bash)](https://blog.csdn.net/FreeApe/article/details/46845555)

[^ref4]: [Metadata - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/extensions/metadata/#usage)

[^only-ssh-connect]: GitHub has deprecated password-based authentication over HTTPS; connections must use SSH or a Personal Access Token. See [Which remote URL should I use?](https://docs.github.com/en/github/using-git/which-remote-url-should-i-use), [Creating a personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token), and [Connecting to GitHub with SSH](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh).
