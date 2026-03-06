# HR Email Campaign Workflow

## Description
Autonomous pipeline for identifying HR contacts at target companies, verifying their email addresses, and sending personalized outreach campaigns.

## Triggers
- **Manual**: `@Nanobot start HR campaign for [Target Companies List]`
- **Scheduled**: Every Tuesday at 10 AM.

## Steps

### 1. Lead Generation
- Uses `Hunter.io` or `Apollo` skills to find email addresses associated with company domains.
- Filters for keywords: "HR", "Talent Acquisition", "Recruiting", "Engineering Manager".

### 2. Verification
- Performs SMTP verification to ensure the email address is valid and won't bounce.
- Checks against a "Do Not Contact" list.

### 3. Personalization
- Claude analyzes the contact's LinkedIn profile or company news.
- Generates a tailored draft highlighting the user's specific value proposition.

### 4. Sending
- Routes the email through a pool of authenticated Gmail/Outlook accounts to avoid rate limits.
- Staggers sends over several hours.

### 5. Tracking
- Monitors for replies and updates the `OUTREACH_TRACKER.md` file.
- Notifies the user on Telegram if a reply is received.

## Safety
- Requires user approval for the first 5 drafts of any new campaign.
- Enforces a strictly rate-limited "Cooldown" period between sends.
