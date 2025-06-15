# Correct `created` Timestamp Script

## Overview

This script is designed to correct the `created` timestamp in markdown files
that were imported into Obsidian from Day One. During the import process,
Obsidian's linter plugin assigned an incorrect `created` timestamp, which needs
to be corrected to accurately reflect the original creation date of the notes.
The script uses the `date` field, which contains the correct date, to update
the `created` field while preserving its original format.

## Background

- **Day One to Obsidian Export**: I exported my notes from Day One, a
  journaling application, to Obsidian, a markdown-based note-taking tool.

- **Incorrect Timestamp Issue**: During the import process, Obsidian's linter
  plugin inadvertently assigned an incorrect `created` timestamp to the notes.
  This has affected the usefulness of the `created` field for searching and
  indexing purposes within Obsidian.

- **Correct `date` Field**: Fortunately, the exported notes still contain a
  `date` field that correctly represents the original creation date of each
  note.

- **Solution**: This script corrects the `created` field using the value from
  the `date` field, ensuring consistency and accuracy across all notes.

## Script Functionality

- The script reads each markdown file in a specified directory (and its
  subdirectories).

- It locates the YAML front matter, which contains the metadata of the note.

- It reads the `date` and `created` fields and uses the value from `date` to
  correct the `created` field.

- The format of the `created` field is preserved, whether it's in
  `YYYY-MM-DDTHH:MM:SS` or `YYYY-MM-DD HH:MM:SS`.

## Usage

### Prerequisites

- Ensure you have Python installed (version 3.x).

- Backup your markdown files before running this script, as it modifies the files in place.

### Running the Script

1. Save the script to a file, e.g., `correct_created.py`.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script with the directory containing your markdown files as an argument:

   ```bash
   python correct_created.py /path/to/markdown/files
   ```

   Replace `/path/to/markdown/files` with the path to the directory where your markdown files are stored.

4. The script will process all `.md` files in the specified directory, including its subdirectories, and update the `created` field.

### Example

Given a markdown file with the following front matter:

```markdown
---
created: 2024-09-05T12:11:44
date: 2018-05-25 21:39:30 Friday
title: A Note on Productivity
---
```

After running the script, the front matter will be updated to:

```markdown
---
created: 2018-05-25T21:39:30
date: 2018-05-25 21:39:30 Friday
title: A Note on Productivity
---
```

## Important Notes

- **Backup Your Files**: The script modifies files directly, so it's recommended to back up your files before running the script.
- **File Encoding**: The script uses UTF-8 encoding to handle special characters properly.
- **Recursive Operation**: The script processes all markdown files in the specified directory and its subdirectories.

## Error Handling

- If the script cannot parse the `date` or `created` fields, it will print an error message indicating the issue.
- If the YAML front matter is missing or not at the beginning of the file, the script will not make any changes and will notify you accordingly.

## Requirements

- Python 3.x

## Contact

If you encounter any issues or have questions regarding this script, feel free to reach out!
