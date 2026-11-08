# Fact Reels: library and publisher

A browsable library of short fact videos: https://lorneh12.github.io/fact-reels/

- **Browse:** rows by topic and status, search, sort, and hover previews.
- **Watch and download:** the video, thumbnails, caption and caption track.
- **Publish manually:** "Share to app" on a phone, or a platform button that copies the caption, downloads the video and opens the upload page.
- **Publish automatically to Instagram:** "Post to Instagram" opens a pre-filled `publish:` issue. When the **repo owner** submits it, `.github/workflows/publish.yml` posts the Reel through the Instagram Graph API and marks it Posted.

## One-time setup for automatic posting

1. Use an Instagram **professional** account (Business or Creator) linked to a Facebook Page.
2. Create a Meta app with `instagram_basic` and `instagram_content_publish`, and get a **long-lived** access token.
3. In this repo, go to Settings > Secrets and variables > Actions and add the secrets `IG_USER_ID` and `IG_ACCESS_TOKEN`. Optionally add the variable `IG_GRAPH_VERSION`.

Without the secrets, every request is a **dry run**: the issue gets a log of what would have been posted.

Long-lived tokens expire after about 60 days, so refresh yours before then.
