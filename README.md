# Ontograph

A 3D ontology viewer and editor. Things are drawn as glowing blobs with their names inside, relations as 3D tubes, in a dark or light theme. It was built as a voice-driven tool hosted inside Claude; this repository holds the runnable files.

## Run it

**Simplest:** download `ontograph-standalone.html` and open it in Chrome or Edge. It is one file with everything inside. Fonts load from Google Fonts when you are online and fall back to system fonts when you are not.

**From source:** keep `index.html` and `vendor.js` in the same folder and open `index.html`, or serve the folder (for example `python3 -m http.server`) or publish it with GitHub Pages.

## What works outside Claude

| Works anywhere | Needs the page hosted in Claude |
| --- | --- |
| Explore in 3D: rotate, zoom, click a node | Voice input |
| Concept map and formal ontology views, OWL/Turtle output | Turning spoken or typed sentences into new nodes and relations |
| Rename, change kind and delete in the inspector; undo | "Tidy up" |
| Save in the browser, several named ontologies | Saving to a Claude account |
| Export and import (below) | |
| Typed commands: `focus on hospital`, `formal view`, `light mode`, `undo`, `fit view`, `save`, `export`, `import` | |

So a standalone copy can open, explore, edit and re-export an ontology, but it cannot add new things: that step uses Claude.

## Save, export, import

- **Save** keeps the ontology in this browser's storage (`localStorage`). It is per browser and per machine. Changes also save automatically.
- **Export → Ontograph file** downloads a `.json` file holding everything. This is the file to keep, share and import back in.
- **Export → OWL / Turtle** downloads a Turtle file for ontology tools (`.ttl`, or `.ttl.txt` from the page hosted in Claude). Class-to-class relations are written as `owl:someValuesFrom` restrictions; review it before using it in a formal OWL toolchain.
- **Import** opens an Ontograph `.json` file or a Turtle file as a new ontology. Choose a file, drop one on the page, or paste the text. Turtle written by Ontograph comes back intact, with one quirk: a class description written as `key: value` is read back as a property. Other Turtle or OWL files are read on a best-effort basis: classes, individuals, labels, comments, subclass and type links, object properties with a domain and range, and simple property values.

### Ontograph file format

```json
{
  "format": "ontograph",
  "version": 1,
  "name": "Example",
  "entities": [
    { "id": "hospital", "label": "Hospital", "kind": "class", "description": "optional", "props": { "optional": "values" } },
    { "id": "northfield_general", "label": "Northfield General", "kind": "individual" }
  ],
  "relations": [
    { "source": "northfield_general", "target": "hospital", "type": "instanceOf" },
    { "source": "hospital", "target": "department", "type": "property", "label": "has" }
  ]
}
```

`kind` is `class` or `individual`. `type` is `subClassOf`, `instanceOf` or `property`; only `property` carries a `label`.

## Files

| File | What it is |
| --- | --- |
| `ontograph-standalone.html` | The whole tool in one file |
| `index.html` | The page: layout, themes, 3D scene, editing, save/export/import |
| `vendor.js` | Bundled libraries, unmodified: three.js 0.186.1, 3d-force-graph 1.80.1, three-spritetext 1.10.0 and their dependencies |
| `build_standalone.py` | Rebuilds the standalone file: `python3 build_standalone.py index.html vendor.js ontograph-standalone.html` |

## Third-party code

`vendor.js` (also inlined in the standalone file) bundles [three.js](https://github.com/mrdoob/three.js), [3d-force-graph](https://github.com/vasturiano/3d-force-graph) and [three-spritetext](https://github.com/vasturiano/three-spritetext), each published by its authors under the MIT licence. See those projects for the licence text.
