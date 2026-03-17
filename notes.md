# HarperBot big-diff test

This commit intentionally changes multiple files so HarperBot can:

- create a review
- post inline comments
- respond to `/analyze`, `/apply`, `/merge` commands

## Things to look for

- suggestions that remove `== None`
- suggestions about regex escaping and style
- suggestions about docstrings and naming

