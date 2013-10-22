#MenuTitle: Remove Images
# -*- coding: utf-8 -*-
"""Deletes placed images from selected glyphs."""

import GlyphsApp
Font = Glyphs.font
selectedLayers = Font.selectedLayers

def process( thisLayer ):
	thisLayer.setBackgroundImage_(None)

Font.disableUpdateInterface()

for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	print "Deleting image in", thisGlyph.name
	thisGlyph.undoManager().beginUndoGrouping()
	process( thisLayer )
	thisGlyph.undoManager().endUndoGrouping()

Font.enableUpdateInterface()
