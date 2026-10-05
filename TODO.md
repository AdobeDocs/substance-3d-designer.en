# TODO

## Tools

* Templates for directory pages + script to update pages based on current hierarchy
* Update existing node pages to a provided template

## Additions

* Entry points for Python API documentation on AdobeDocs
* Examples in 'Documentation pop-up' page
* Glossary:
  * HDR
  * Metalness / Metallic
  * HDR
  * Specular
  * Height map
  * Opacity
  * Frustum
  * Tangent space
  * Seed / Random seed
  * FX-Map
  * Pixel processor
  * Preset
* Update AGENTS.md and skills to manage:
  * Images: centering, zooming
  * Tables: auto/fixed layout, text alignment
* DESIGNER-12465: `Refine level` parameter is inert when Height map is absent or flat
* DESIGNER-12652: Point users to performance troubleshooting guide for OpenGL renderer
* DESIGNER-11866: Tonemapping functions
* DESIGNER-10655: Add examples + references to sample projects for Pixel processor and FX-Maps


## Fixes

* Fix size of icons in [overview.md](help/getting-started/overview/overview.md)
* Fix broken image in `BnW spots 2` page
* Fix link for 1st example image in node pages (E.g. new noises)

## Investigate

* Before/after component

## Learning hub (`learning` branch)

- Understand what blocks downloading SBS files (Asked [here](https://adobe-3di.slack.com/archives/CMF1JGMLY/p1790005804708379))
- Understand how we can live-test pages without being public-facing or included in ToC
- Explorer filtering options for list of samples: Microsite? ([Example](https://experienceleague.adobe.com/en/tools/campaign-error-codes))
- Automate building sample item
  - Ingest metadata from file (JSON, YAML, ...)
  - Inline thumbnail (click to enlarge)
  - Complexity marker in sample items
- Provide sample authors with SBS validation tool
- Mention downloadable SBS files from 3D assets (with active subscription)

Microsite for glossary?