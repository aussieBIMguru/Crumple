# Crumple

**A Python-based Dynamo package for Revit, with 300+ custom nodes.**

**Current version:** `2026.8.1`

Crumple is a **Dynamo package for Autodesk Revit** (2023–2026), built around everyday model management and delivery automation for architects. It's general-purpose in scope, but most nodes exist to solve a specific practical problem encountered in production Revit/Dynamo work.

> **📌 Status: legacy / maintenance only.** Crumple remains available on the Dynamo Package Manager and will keep working in existing graphs, but it is no longer where active development happens. **[Pickles](https://github.com/aussieBIMguru/Pickles)** is its spiritual successor — a ground-up C#/ZeroTouch rebuild of the same ideas — and is where new features, fixes and future nodes will land. If you're starting something new, start there.

## ✨ Features

Crumple's nodes are almost entirely written in **CPython3** (the Python engine bundled with Dynamo), with no IronPython dependency. Broadly, the package covers:

* **Revit document & unit utilities** — unit conversions, document/version info, workshared status, current view/selection.
* **Collectors** — one-node collection for most common Revit categories and types (sheets, views, worksets, materials, patterns, schedules, links, CAD, and more).
* **Views, sheets & schedules** — creating, querying and editing views, sheets, viewports, view templates and schedule data.
* **Rooms, spaces & areas** — lookups by point/number, boundaries, tagging, and area/space creation.
* **Family document automation** — batch-opening family documents, reading and writing parameters, types and formulae across many families at once.
* **General data & list utilities** — string, list, math and date/time helpers aimed at cleaning up everyday graph plumbing.
* **System & file utilities** — user paths, file/directory helpers, delimited file and Excel (pandas) read/write.
* **Small UI helpers** — simple message boxes and file/path prompts for scripted graphs.

### Node coverage

| Category | Nodes | Examples |
| --- | :---: | --- |
| Collect | 39 | Sheets, Views, Worksets, Materials, Patterns, RevitLinks, Schedules |
| Revit / Document | 23 | Unit conversion, GetDocument, ExportToPdf/Dwg, Version, Selection |
| Element(s) | 27 | ById, Centroid, Owners, Workset, IsolateInView, Rename |
| View / Viewport / ViewFamilyType / ViewSheetSet | 29 | CreatePlans, ApplyTemplateByName, GetCropBox, Create |
| Family / FamilyDoc / FamilyParam / FamilyType / FamilyInstance | 30 | GetParameterValues, SetParameterValues, SaveAs, ReportToValues |
| String | 16 | Regex, CipherTo/From, RevitLegal, ToMatrix |
| List | 12 | SplitAtValue, KickFlip, GraftByPrimary, TryToGetItemAtIndex |
| Sheet | 9 | Create, GetByNumber, Revisions, NameFormatted |
| Room / Space | 10 | AtPoint, Boundaries, TaggedInView, CreateUnplaced |
| Math | 8 | RandomNumbers, ClosestNumber, Fibonnaci, Ordinals |
| ScheduleType | 8 | DataAsText/Values, Headers, RenameHeaders |
| File / Directory / System | 17 | ReadDelimited, UserPaths, TempFiles, FilterBackups |
| SharedParameters | 6 | Create, Flat, Grouped, Repath |
| Audit | 6 | Views, ViewTemplates, ViewFilters, ScheduleTypes |
| Coordinates / Vector / Point | 9 | PBP, Origin, GroupByDirection, Deconstruct |
| Flow / Timer / UI | 11 | IfThenElse, WaitFor, Delay, Messenger |
| Excel | 3 | Read, Write, SheetNames (via pandas) |
| Everything else | ~35 | Doors, Stairs, Walls, Groups, ScopeBoxes, Warnings, and other one-off utility nodes |

That's roughly **314 nodes** in total across the package.

## 📦 Installation

Crumple is available through the **Dynamo Package Manager** — search for **Crumple** and install it directly into Revit 2023–2026.

## 💻 Development

Crumple is built as a collection of Dynamo custom nodes (`.dyf` files), each wrapping one or more embedded CPython3 scripts. Because a `.dyf` is just JSON under the hood, the whole package can be browsed, diffed and read the same way you'd read any `.json` file — no compiler or build step needed to inspect how a node works.

The full source is available on GitHub for anyone who wants to look under the hood, though — as noted above — it's kept in maintenance mode rather than active development.

## 📄 License

Crumple is released under the **MIT License**.

You are free to use, modify and distribute the software in accordance with the terms of the license.

## 🔗 Links

**Website / Tutorials:**
https://www.youtube.com/aussiebimguru

**Source Code:**
https://github.com/aussieBIMguru/Crumple

**Successor package:**
https://github.com/aussieBIMguru/Pickles

---

Made by **Gavin Nicholls (ex Crump) / Aussie BIM Guru**