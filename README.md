# Obsidian Ridge Labs apps for Atlassian: public pages

Support, documentation, privacy and security pages that the Atlassian Marketplace listings link to. Plain static HTML, hosted free on GitHub Pages.

- Edit the page bodies in `pages/`, then run `python3 build.py` to write the `index.html` files. Commit both.
- A new app gets `pages/<app>.html` (copy `pages/jira-gantt.html`), a block on `pages/home.html`, and a section in `pages/privacy.html` that says what it reads, where it goes, and what it keeps.
- No em or en dashes; `build.py` refuses them.

URLs once published (GitHub Pages, repo `obsidian-ridge-apps`, branch `main`, folder `/`):

| Page | URL | Used for |
| --- | --- | --- |
| Apps and support | https://amotor-ai.github.io/obsidian-ridge-apps/ | Partner profile support URL (`#support`) |
| Gantt documentation | https://amotor-ai.github.io/obsidian-ridge-apps/jira-gantt/ | Version "Documentation URL" |
| Privacy policy | https://amotor-ai.github.io/obsidian-ridge-apps/privacy/ | Privacy and Security tab, partner profile |
| Security policy | https://amotor-ai.github.io/obsidian-ridge-apps/security/ | Privacy and Security tab |

To move these to a subdomain such as `apps.obsidianridgelabs.com` later: add a `CNAME` file with that name, add a CNAME DNS record pointing to `amotor-ai.github.io`, and update the URLs in each listing.
