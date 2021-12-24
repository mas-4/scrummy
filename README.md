# Scrummy

Scrummy is a WIP.

It aims to be a plaintext cli todo management system in the vein of such beloved unixy productivity tools as

- [pass](https://www.passwordstore.org/)
- [ledger](https://www.ledger-cli.org/) and [hledger](https://hledger.org/)
- [taskwarrior](https://taskwarrior.org/)

I'm writing this software exclusively for my own use, but trying to keep it as professionally designed as possible.

# Usage

Scrummy is a click cli application and has only one command for now:

```commandline
scrummy rollover
```

If your configuration file is correctly set and your directory structure is correct, it will take your `todo.md` file,
match each todo item's id number with an id in an "epic" file, and check it off and date it with the completion date if
its completed.

It will then create a new todo file with the completed items removed and archive the old todo.

Adding todo items is (and will likely remain) a manual process. Id numbers are manually created as well.

# Configuration

I hate home folder dot files, so I'm using a config file in the xdg system. Currently, I imagine this does not work on
Windows.

Configuration lives in `$XDG_CONFIG_HOME/scrummy/scrummyrc`

There are only a handful of configuration options:

```
home=~/documents/scrummy
todo_filename=todo.md
max_line_length=80
indent_size=2
date_format=%Y/%m/%d
list_indicator=-
```

# Directory Structure and Workflow

Currently, the directory structure for "home" where your todo and epic files live is:

```
.
├── checklists
│   ├── 2021-12-19.md
│   ├── 2021-12.md
│   ├── 2021.md
│   ├── archive
│   ├── monthly.md
│   ├── weekly.md
│   └── yearly.md
├── scrum
│   ├── 101-christmas-2021.md
│   ├── 102-smart-apartment.md
│   ├── 104-finances.md
│   └── 105-scrummy.md
├── sprints
│   ├── 2021-12-21.md
│   └── 2021-12-24.md
└── todo.md
```

The checklists system currently doesn't do anything, but my intention is to have similar rollover for them.
Documentation will be made for that feature after it is implemented.

Currently, a scrum file should look like this:

```markdown
---
title: Smart Apartment description: Setting up a smart pseudo-apartment id: 102
---

- [ ] 102-0 Clean table
- [ ] 102-1 Furniture
    - [x] 102-11 Assemble cocktail table (Thursday)
    - [ ] 102-12 Another trash can
    - [ ] 102-13 Decide on ac unit
- [ ] 102-3 Clean up wire closet (Saturday)
- [ ] 102-4 Smart Home
    - [ ] 102-41 Install home assistant on Raspberry Pi
    - [ ] 102-42 Compile list of automatables
        - [ ] 102-430 Design and consider auto watering units
        - [ ] 102-431 Music integration
        - [ ] 102-432 Lights
        - [ ] 102-433 Acquire one other raspberry pi 4
- [ ] 102-5 Scrum Integration
    - [x] 102-51 Get a taskflow for moving items into the todolist
    - [ ] 102-54 Checklists and integrations.
        - [x] 102-540 Create first checklist for monthly tasks with dates
          (2021/12/21)
    - [x] 102-52 See about forking the kde plasmoid for this work flow or finding a better tool.
    - [ ] 102-53 See about home assistant integrations with text. I imagine I just write something myself.
    - [x] 102-55 Maybe using obsidian?
    - [ ] 102-56 Get used to the task flow of todo sprint/scrum
    - [x] 102-57 Revolving monthly checklist with dates and yearly (2021/12/21)
```

Then a `todo.md` file will look like this:

```markdown
# 2021-12-24


* [ ] Meet with mark for setting up github
* [ ] 102-0 Clean table
* [ ] 102-56 Get used to the task flow of todo sprint/scrum
* [ ] 101-021 Wrap chris wine and nametag
* [ ] 101-022 Wrap mom wine and nametag
* [ ] Switch over domain
* [ ] Write script for migrations
* [ ] check marketplace app
* [ ] Update lock screen
* [ ] 104-030 Activate debit card
* [ ] 101-0 Complete gifts
    * [ ] 101-02 Wrap gifts
    * [ ] 101-021 Wrap chris wine and nametag
    * [ ] 101-022 Wrap mom wine and nametag
    * [ ] 101-023 Wrap betsy dvd and nametag
    * [ ] 101-024 Wrap betsy book and nametag
    * [ ] 101-03 Cards for everyone
    * [ ] 101-031 Compile list of cards
    * [ ] 101-04 Update spreadsheet
* [ ] 102-56 Get used to the task flow of todo sprint/scrum
```

Right now my list indicators are inconsistent, this isn't important for scrummy's operations (though its currently
dependent on either an asterisk or a dash), but it will write out whatever list_indicator you configure.

At the end of the day, when you run `scrummy rollover`, the todo file will be read, any checked off items will be
updated in the `scrum/epic.md` files as completed and a date of completion will be appended, the todo will be cleared
and archived in sprints, and an identical todo file without the completed items will be written to the root home
directory.

Of course this process is still finicky. I just completed v0.1 yesterday.

Unnumbered items in the todo file will just be ignored and carried over to the next file if they are not completed.

Anything written in this file that isn't of this format will be ignored and kept in the archived todo file (it's just a
move operation)
