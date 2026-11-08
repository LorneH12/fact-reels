# Fact Reels: library and publisher

A browsable library of short fact videos: https://lorneh12.github.io/fact-reels/

- **Browse:** rows by topic and status, search, sort, and hover previews.
- **Watch and download:** the video, thumbnails, caption and caption track.
- **Publish manually:** "Share to app" on a phone, or a platform button that copies the caption, downloads the video and opens the upload page.
- **Publish automatically to Instagram:** "Post to Instagram" opens a pre-filled `publish:` issue. When the **repo owner** submits it, `.github/workflows/publish.yml` posts the Reel through the Instagram Graph API and marks it Posted.

## One-time setup for automatic posting (about 15 minutes)

1. **Instagram:** make the account professional. In the app, go to Settings > Account type and tools > Switch to professional account (Creator or Business).
2. **Meta app:** go to https://developers.facebook.com > My Apps > Create app, and choose the Instagram use case ("Instagram API with Instagram Login").
3. **Token:** in the app's Instagram > API setup with Instagram login, add your Instagram account and generate a token, allowing `instagram_business_basic` and `instagram_business_content_publish`. Copy the **access token** and your **Instagram user ID**. The app can stay in development mode for posting to your own account.
4. **GitHub:** in this repo, go to Settings > Secrets and variables > Actions.
   - **Secrets:** add `IG_USER_ID` and `IG_ACCESS_TOKEN`.
   - **Variables:** add `IG_GRAPH_HOST` = `graph.instagram.com`.

   If you use the older Facebook Page setup, leave `IG_GRAPH_HOST` unset.

Without the secrets, every request is a **dry run**: the issue gets a log of what would have been posted.

Tokens expire after about 60 days, so generate a new one and update the secret before then. A failed post comments the API error on the issue.
