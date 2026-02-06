---
title: "Spot Colors (Pantone)"
description: ""
helpx_description: "Designer > Color Management > Spot Colors (Pantone)"
---

# Spot Colors (Pantone)

Spot Colors are an alternative mode for choosing colors. Instead of the standard RGB or HSV color picker, Substance 3D Designer lets you choose colors from Color Books, matching existing color management and reproduction systems. This allows you to ensure digital colors used in Designer, closely match those of manufactured products.

Currently Spot Colors offers seventeen Pantone books.

## Color management

Since Spot Colors are meant for accurate color reproduction and matching, it's essential you set up[ Color Management](../color-management.md) for Designer before you start working. Spot Colors work best with <b>Adobe Color Engine (ACE)</b> Color Management, not with OCIO. They will work with legacy mode but you can not be sure they are displayed correctly if your monitor is not calibrated for sRGB.

In short, setting up Color Management for Spot Colors involves the following:

* Calibrate you monitor by generating or obtaining the proper ICC profile.
* Enable Color Management with Adobe Color Engine (ACE) in Designer's Preferences.
* Set 2D and 3D View to use the proper profile from your monitor.
* Restart for changes to take effect.
* Verify color match between Designer and another Adobe application such as Adobe Illustrator or Photoshop. The color "<b>Pantone Rhodamine Red C</b>" from the first Pantone book, Solid Coated, is a good test case as it can vary significantly if color management is not correct.

>[!WARNING]
>
> **Thumbnail Colors**
> 
> Node thumbnails are *not Color Managed by default*, so only trust color display in the 2D View with the correct profile. Thumbnail Color Management can be enabled in the Preferences under your Project's Color Management, but it comes at a slight performance cost.

## Using Spot Colors

### Switching to Spot Color from RGB

Even if you set up Color management, color pickers still default to RGB or HSV color pickers by default. You need to switch them to Spot Colors manually. This setting is stored per parameter and even carries over when exposing a parameter.

1. Click the ![](image2021-1-25-9-40-40.png) <b>Color picker type</b> button next to the RGB color swatch.
1. Instead of <b>RGB colors</b>, choose any <b>Color book</b> from the dropdown list.
1. The icon of the ![](image2021-1-25-9-40-25.png) <b>Color picker type</b> changes, and its interface changes to <b>Spot color</b> mode.

![Switching to Spot color mode](spot-switch.gif "Switching to Spot color mode"){width="512px"}

### Choosing and finding Spot Colors

There are a few ways to find and choose Spot colors within a color book.

* You can use the ![](image2021-1-25-10-40-28.png) ![](image2021-1-25-10-40-53.png) <b>Left and Right arrows</b> on either side of the book's pages to flip between pages. You can also click and drag on the page display to scroll between pages.
* You can click on any color from the current page to pick it. Often, more colors are available and require scrolling down a bit.
* You can use the search bar to search color by name or number. This search only matches the names of colors in the book, there's no complex logic going on; searching "gray" will only yield results with the word "gray" in their name, you won't see any gray colors that only have numbers in their name.
* To get a bigger, easier to use interface for the color book, click the color preview box between the ![](image2021-1-25-10-39-18.png) <b>Eyedropper</b> icon  and the ![](image2021-1-25-10-40-28.png) <b>Left arrow</b>.

![Browsing Spot colors](spot-choose.gif "Browsing Spot colors"){width="512px"}

### Picking and Converting Spot Colors

Spot Colors can be picked using the ![](image2021-1-25-10-39-18.png) <b>Eyedropper</b> tool. When in Spot Color mode this means the sampled RGB color will be converted to the closest matching Spot Color from the currently selected book.

Designer's <b>Eyedropper</b> tool can be used anywhere on your screen without limitations, so this means you can use Designer as Spot Color conversion tool,

Switching Books, or even switching back to RGB from a Spot Color book will convert the current color to the closest match. This means you can convert colors between books and back to RGB.

>[!WARNING]
>
> Converting Spot Colors between books is a lossy operation. Making a round-trip conversion will often not lead to the same color as the one you started with!

![Picking and converting Spot colors](spot-pick.gif "Picking and converting Spot colors"){width="512px"}
