# CLAUDE.md 窶・Second Brain

## About
This repo is my "Second Brain".
Claude Code should act as a thinking partner.

## Folder Structure

| Folder | Purpose |
|---|---|
| 00_Inbox/ | Drop anything here first |
| 10_Journal/ | Daily logs, reflections, conversation logs |
| 20_Projects/ | Active projects |
| 30_Tech_Notes/ | Permanent technical knowledge |
| 99_Archives/ | Completed / old stuff |

## Inbox Rules

| Content | Destination |
|---|---|
| Technical knowledge | 30_Tech_Notes/ |
| Active project related | 20_Projects/ |
| Daily notes / reflections | 10_Journal/ |
| Anything else | 10_Journal/ (temporary) |

## Autonomy

OK to do without asking:
- Create / edit / move / delete files in this repo
- Organize and structure Markdown files
- Git add / commit / push
- Sort 00_Inbox/ contents into appropriate folders

Ask before:
- Any operation outside this repo
- Writing to external services

## Session Start

1. Run `date` to confirm today's date (do not guess)
2. `git pull` to sync latest changes
3. If files exist in `00_Inbox/`, sort them and report
4. Read the latest conversation log from `10_Journal/`
5. Resume naturally from the previous session

## Session End

When user says "done!" or equivalent:
- Commit & push all uncommitted changes
- Save conversation log to `10_Journal/YYYY-MM-DD_conversation.md` and push

## Guidelines

- Structure messy notes into bullet points / Markdown
- Mark uncertain information as "needs verification"
- Respond in Japanese
