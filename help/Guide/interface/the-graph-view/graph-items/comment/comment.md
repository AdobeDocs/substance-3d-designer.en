---
title: "Comment | Substance 3D Designer"
description: "Designer > Interface > Graph view > Graph items > Comment"
---

# Comment

<table>
<tr style="border: 0;">
<td width="25.00%" style="border: 0;" valign="top">

![Comment icon](graphatomic-comment.png "Comment icon")

</td>
<td width="100.00%" style="border: 0;" valign="top">

A comment is simply a piece of free-floating text that can be placed anywhere in a graph.

It is intended for annotating and explaining parts of a graph. Its <b>Description</b> property holds the text being displayed.

</td>
</tr>
</table>

>[!NOTE]
>
> Comments have automatic line breaking which aims to minimize their footprint in a graph.

## Creating comments

The default type of comment is placed independently of nodes in the graph.

It may be created in the following ways:

+++Node menu


PressSpacebarin the Graph view to open theNode menu, and select the 'Comment' item in the list.





Type 'comment' in the search field to surface the item and find it more quickly.



+++

+++Shortcut


If a keyboard shortcut is mapped to the 'Comment' item in thePreferences, press that shortcut when the Graph View has focus.



[Preferences](../../../preferences-window/preferences-window.md)

+++

+++Contextual menu


In the Graph View, pressRMBon any object or in empty space and select theAdd Commentoption.



+++

+++Graph toolbar


In the Graph View toolbar, click the 'Comment' button in theNode Palette.



+++

+++Library


In the Library, select theGraph Itemscategory then drag and drop the 'Comment' item into the Graph View.



+++

>[!TIP]
>
> When a comment is created, its 'Description' property automatically gains focus so you can immediately edit the comment's text.

## Parented comments

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">

A parented comment is a comment that is *attached to a specific node* in the graph so that when the node is moved, the comment follows and when the node is deleted, the comment is deleted along with it.

Comment that are created when a *single* node is currently selected, or through a single node's contextual menu, are parented to that node.

</td>
<td width="33.33%" style="border: 0;" valign="top">

![Comments: Parented comments](graph-comment_parented.gif "Comments: Parented comments")

</td>
</tr>
</table>

## HTML formatting

Text can be formatted using HTML tags. This formatting is toggled using the ![](graph-frames_html-markup-button.png) <b>HTML markup</b> button in the comment's <b>Description</b> property.

>[!TIP]
>
> Learn more about this feature in the <b>Description</b> section of the [Frames](../frame/frame.md) documentation.

![Comments: HTML markup](graph-comment_html-markup.gif "Comments: HTML markup")
