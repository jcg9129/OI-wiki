Before we begin: everyone on the **OI Wiki** team warmly welcomes you to contribute pages to this project. It is precisely because of hundreds of people like you that **OI Wiki** is what it is today!

This article mainly describes the writing process for contributing to **OI Wiki**. Before you write or revise a wiki page, please read the following carefully to help you produce higher-quality content.

## Contribution Guidelines

Before editing, please read the [OI Wiki Contribution Guide](https://github.com/OI-wiki/OI-wiki/blob/master/.github/CONTRIBUTING.md) and the [project guidelines](./about.md#project-guidelines) so you can better collaborate and communicate with community contributors.

## Getting Involved

???+ warning "Warning"
    Before you start writing a piece of content, please check the [Issues](https://github.com/OI-wiki/OI-wiki/issues) to confirm that nobody else is doing the same work, then open a [new issue](https://github.com/OI-wiki/OI-wiki/issues/new) to record the content to be written.

???+ tip "Tip"
    There are also many problems to fix/solve in the Issues, especially our Iteration Plan. Picking up a task from there is a great start!

To ensure that entries are professional and accurate, we suggest you consider the following before editing:

1.  **Choose a field you are familiar with**: give priority to editing entries related to your expertise, study background, or interests. This helps you create high-quality content.
2.  **Be cautious with new fields**: if you are still a beginner at a topic or not very familiar with it, we suggest you first deepen your understanding through reading and study, and start editing only once you feel reasonably confident.
3.  **Consult relevant sources**: when adding to or revising an entry, we suggest you first consult authoritative literature and sources to make sure the information is accurate. You are also welcome to ask questions in the page's comment section or in our community, and discuss with other editors.

We value the enthusiasm and effort of every contributor, and we understand that everyone's level of expertise differs. Let us work together to care for this garden of knowledge and help more readers with accurate, professional content. We look forward to your contributions! To quote Wikipedia:

> Don't be afraid to edit — be bold in updating pages! [^ref1]

### Editing on GitHub

Contributing to **OI Wiki** **requires** a GitHub account (you can register on [GitHub's sign-up page](https://github.com/signup)), but it does **not** require advanced GitHub skills. Even if you are a newcomer, you can do an **excellent** job of editing just by following the steps described below.

???+ tip "Tip"
    Until your changes are merged into the main **OI Wiki** repository, none of the modifications you make to **OI Wiki**'s content will appear on the main **OI Wiki** site, so there is no need to worry that your changes will break what is currently shown on **OI Wiki**.

    If you are still unsure, you can check out [GitHub's official tutorials](https://skills.github.com/).

#### Editing a single page

1.  Find the corresponding page on **OI Wiki**.
2.  Click the **"Edit this page"** (<i class="md-icon">edit</i>) button at the top right of the body text (to the left of the table of contents). After confirming that you have read this page and the [format manual](./format.md), click the button and follow the prompts to jump to GitHub to edit.
3.  Write the content you want to change in the edit box. Note that during editing and the subsequent commit process, please **turn off your automatic translation software**, as it may cause unnecessary trouble (for example, the file you are editing may sometimes be renamed incorrectly, affecting the directory structure).
4.  When you are done, scroll to the bottom of the page, fill in the commit message following the [commit message format](#commit-message-format) in this article, then click the **Propose changes** button to submit. After you click the button, GitHub will automatically create a branch of the **OI Wiki** repository for you and add your commit to that branch.
5.  GitHub will automatically redirect to your branch's page, where a green **Create pull request** button appears at the top. Click it and GitHub will take you to a pull-request creation page. Scroll down to check that your changes are correct, write the pull-request description following the [pull request message format](#pull-request-message-format) section of this article, and then click the green **Create pull request** button to create the pull request.
6.  All being well, your pull request is now submitted to the repository. Just wait for an administrator to review it and merge it into the main repository.

While waiting for the merge, you can comment on, upvote, or downvote other people's pull requests. If there is a new message, a notification will appear at the top right of the page, along with an email reminder (depending on the notification method configured in your personal settings).

#### Editing multiple pages

If you need to edit the content of multiple unrelated pages at once, please modify all pages one at a time following the [Editing a single page](#editing-a-single-page) section above.

1.  Open the [OI-Wiki/OI-Wiki](https://github.com/OI-Wiki/OI-Wiki) repository, press the <kbd>.</kbd> key on your keyboard (or change `github.com` in the URL to `github.dev`) [^ref2] to enter GitHub's web-based VS Code editor.
2.  Make changes to the page source files in the editor. You can use the preview button at the top right of the page (or press the <kbd>Ctrl+K</kbd> <kbd>V</kbd> shortcut) to open a preview pane on the right.
3.  When you are done, use the Source Control tab on the left, fill in the commit message following the [commit message format](#commit-message-format) in this article, and commit. When committing, you will be prompted whether to create a branch of the repository; click the green **Fork Repository** button.
4.  After committing, a prompt box will pop up at the top center of the page. Fill in the title in the first prompt box and the branch name within the repository that this commit should go to in the second prompt box. A prompt box will then pop up at the bottom right with content similar to `Created Pull Request #1 for OI-Wiki/OI-Wiki.`; click the blue link to view the pull request.

#### Appending changes to a pull request

1.  Open the [OI-Wiki pull request list](https://github.com/OI-wiki/OI-wiki/pulls), find the pull request you submitted, and click it.
2.  Below the title on the pull-request page there will be a line such as `<your ID> wants to merge x commits into OI-wiki:master from <your ID>:patch-1`; click the `<your ID>:patch-1` part.
3.  You should be redirected to your branch, and the branch name at the top left of the file list is the branch from which you submitted the pull request (`patch-1` in this example).
4.  Make the changes you need.
    -   If you need to edit a single file or the content of multiple unrelated pages, find the file you want and change it directly. When done, scroll to the bottom of the page, fill in the commit message following the [commit message format](#commit-message-format) in this article, then click the **Commit changes** button to submit.
    -   If you need to edit multiple files, press the <kbd>.</kbd> key on your keyboard (or change `github.com` in the URL to `github.dev`) [^ref2] to enter GitHub's web-based VS Code editor and make the changes. Then use the Source Control tab on the left, fill in the commit message following the [commit message format](#commit-message-format) in this article, and submit your changes.
5.  Your changes are now automatically appended to your pull request.

### Editing locally with Git

???+ warning "Warning"
    For most users, we recommend editing with GitHub's web editor described above.

Although in most cases you can edit directly on GitHub, for some special situations (such as needing a GPG signature) we recommend editing locally with Git.

The general process is as follows:

1.  Fork the main repository into your own account.
2.  Clone the forked repository to your local machine.
3.  Make changes locally and commit them.
4.  Push these changes to your forked repository.
5.  Submit a pull request to the main repository.

For detailed instructions, see the [Git](../tools/git.md) page.

#### Appending changes to a pull request

Continue making changes in the local branch you cloned, then commit and push them. Your changes will be automatically appended to the pull request.

### Previewing changes in the built site

At the bottom of the pull-request page you can find test pages. Click the Details link of the netlify/oi-wiki/deploy-preview item (as shown below) to enter an automatically built preview of your changed pages.

![deploy\_preview](./images/deploy_preview.png)

### Changes to the nav and links

Normally, if you need to add a new page or change the link of an existing page in the navigation, you need to make changes to the [`mkdocs.yml`](https://github.com/OI-wiki/OI-wiki/blob/master/mkdocs.yml) file.

You can refer to the existing format when adding a new page. However, unless you are refactoring or correcting a term, **we do not recommend changing the reference links of existing pages**; unnecessary changes in a pull request will also be rejected.

If you insist on changing a link, please remember to update the author field and the redirect file.

### The author field

The GitHub API cannot track statistics after a file's path changes, so we manually maintain an author list in the file header to solve this problem. The author field is at the very beginning of the Markdown file, in the form `author: Ir1d, cjsoft`, with adjacent IDs separated by a comma and a space. The IDs here are GitHub usernames, i.e. the address of the GitHub profile (for example, `Ir1d` in <https://github.com/Ir1d>).

When changing a link, you need to fill the current page's contributors one by one into the author field.

### Redirect file

When changing a link, to avoid dead links from off-site references, you need to modify the redirect file.

The [`_redirects`](https://github.com/OI-wiki/OI-wiki/blob/master/docs/_redirects) file is used to generate the [Netlify configuration](https://docs.netlify.com/routing/redirects/#syntax-for-the-redirects-file) and the [files used for redirection](https://github.com/OI-wiki/OI-wiki/blob/master/scripts/gen_redirect.py).

Each line represents a redirect rule, writing the source and destination URLs of the redirect (without the domain):

```text
/path/to/src /path/to/desc
```

Note: all redirects are 301 redirects, and only need to be modified when changing a URL in the navigation would cause a dead link.

### Commit message format

For the commit message you need to fill in when committing, please observe the following basic requirements:

1.  The commit summary should briefly describe what this commit changes. Note that the commit summary should not exceed 50 characters; anything beyond that is automatically placed in the body.
2.  If you need to describe the commit further, please explain in detail in the body.

For the commit summary, we recommend the following format:

```text
<change type>(<file name>): <what was changed>
```

Change types fall into the following categories:

-   `feat`: for adding content.
-   `fix`: for correcting errors in existing content.
-   `refactor`: for refactoring a page (larger-scale changes).
-   `revert`: for reverting previous changes.

### Pull request message format

For pull requests, please observe the following requirements:

1.  The title should state the purpose of this PR (**what** work was done, **what** problem was fixed).
2.  The description should briefly narrate what was changed. If it fixes an issue, please add a `fix #xxxx` field in the description, where `xxxx` is the issue number.
3.  Please read the [Contribution Guide](https://github.com/OI-wiki/OI-wiki/blob/master/.github/CONTRIBUTING.md) and the [Code of Conduct](https://github.com/OI-wiki/OI-wiki/blob/master/CODE_OF_CONDUCT.md) carefully, and after agreeing, check the box in the PR template to indicate that you agree to the above guide and code.

For the pull-request title, we recommend the following format:

```plain
<change type>(<file name>): <what was changed> (<corresponding issue number>)
```

Change types fall into the following categories:

-   `feat`: for adding content.
-   `fix`: for correcting errors in existing content.
-   `refactor`: for refactoring a page (larger-scale changes).
-   `revert`: for reverting previous changes.

Examples:

-   `fix(ds/persistent-seg): 修改代码注释使描述更清晰`
-   `fix: tools/judger/index 不在目录中 (#3709)`
-   `feat(math/poly/fft): better proof`
-   `refactor(ds/stack): 整理页面内容`

### Collaboration workflow

1.  After a new pull request is received, GitHub sends an email to the reviewers.
2.  At the same time, two sets of tests run on [GitHub Actions](https://github.com/OI-wiki/OI-wiki/actions) and [Netlify](https://app.netlify.com/sites/oi-wiki), which sync their progress at the bottom of the PR page. GitHub Actions is mainly used to confirm that the changes in the PR will not affect the site build process; Netlify builds the updates in the PR so reviewers can review them (click Details after the tests finish to learn more).
3.  A reviewer may find problems and offer a `review` or `suggested changes` (shown as a gray icon) / `requested changes` (shown as a red icon, appearing only when the reviewer has write access to the repo). Generally, the reviewer will also attach suggestions and the changes to be made. At this point, you will need to keep appending further changes to the pull request. For how to do this, see the `Appending changes to a pull request` part of the `Editing on GitHub` or `Editing locally with Git` sections.
4.  Only after enough reviewers vote to approve a PR can it be merged into the master branch.
5.  After merging into the master branch, GitHub Actions rebuilds the site content and updates the gh-pages branch.
6.  Only then does the server pull the updates from the gh-pages branch and redeploy the latest content.

## References and Notes

[^ref1]: [Wikipedia: Getting Started / Editing](https://zh.wikipedia.org/wiki/Wikipedia:%E6%96%B0%E6%89%8B%E5%85%A5%E9%96%80/%E7%B7%A8%E8%BC%AF)

[^ref2]: [Web-based editor - GitHub Codespaces - GitHub Docs](https://docs.github.com/en/codespaces/developing-in-codespaces/web-based-editor)
