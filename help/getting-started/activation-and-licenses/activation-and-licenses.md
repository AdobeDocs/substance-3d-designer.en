---
title: "Activation and licenses"
description: ""
helpx_description: "Designer > Getting started > Activation and licenses"
---

# Activation process per application type

The activation process depends on where you purchased or have access to Designer:

| Edition | Activation process |
| --- | --- |
| Creative Cloud Desktop | See the dedicated page in the [HelpX documentation](https://helpx.adobe.com/support/substance-3d-designer.html). In case there are any issues the [Creative Cloud documentation](https://helpx.adobe.com/creative-cloud/user-guide.html) may provide additional answers. |
| Steam | Launch the product directly from your Steam library. |
| Substance (standalone) | See the activation process described below. |

## Activation steps (Substance edition)

### USING THE ACTIVATION WIZARD

Three choices are available:

* <b>Evaluate this product</b>: Legacy trials are no longer available. Instead, you can start a 30 day trial for each Substance 3D application [here](https://www.adobe.com/creativecloud/3d-augmented-reality.html) or with Creative Cloud Desktop. Each trial is independent of the other Substance 3D applications, so you can try them one at a time or all at once.
* <b>Activate using a license file</b>: activate the product with a license file (<b>\*.key</b>) downloaded from your account page on the [Substance 3D website](https://store.substance3d.com/user) before 30 Sep 2022.
* <b>Activate using your account</b>: Legacy substance accounts can no longer be used for activation. [More information about Substance accounts is available here](https://helpx.adobe.com/substance-3d/unlisted/faq-end-of-life-accounts.html).

>[!IMPORTANT]
>
> To install the license file with the Activation Wizard, make sure you run Designer as an administrator and temporarily disable your anti-virus.

![Activation wizard](activation-wizard.png "Activation wizard")

### Manual activation

You can manually activate Designer by putting the license.key file in the following folder:

<table data-preserve-html="true">
<colgroup> <col/> <col/> <col/> <col/> </colgroup><tbody><tr><th style="text-align: left;">Platform</th>
<th style="text-align: left;">Version</th>
<th colspan="2" style="text-align: left;">Path</th>
</tr><tr><td rowspan="4" style="text-align: left;"><b>Windows</b></td>
<td rowspan="2" style="text-align: left;"><b>11.2</b> or higher</td>
<td style="text-align: left;">AppData &gt; Local</td>
<td style="text-align: left;">C:&#92;Users&#92;&#91;username&#93;&#92;AppData&#92;Local&#92;Adobe&#92;Adobe Substance 3D Designer</td>
</tr><tr><td style="text-align: left;">AppData &gt; Roaming</td>
<td style="text-align: left;">C:&#92;Users&#92;&#91;username&#93;&#92;AppData&#92;Roaming&#92;Adobe&#92;Adobe Substance 3D Designer</td>
</tr><tr><td rowspan="2" style="text-align: left;"><b>11.1</b> or lower</td>
<td style="text-align: left;">AppData &gt; Local</td>
<td style="text-align: left;">C:&#92;Users&#92;&#91;username&#93;&#92;AppData&#92;Local&#92;Allegorithmic&#92;Substance Designer</td>
</tr><tr><td style="text-align: left;">AppData &gt; Roaming</td>
<td style="text-align: left;">C:&#92;Users&#92;&#91;username&#93;&#92;AppData&#92;Roaming&#92;Allegorithmic&#92;Substance Designer</td>
</tr><tr><td rowspan="2" style="text-align: left;"><b>Mac</b></td>
<td style="text-align: left;"><b>11.2</b> or higher<br/>
</td>
<td colspan="2" style="text-align: left;">/Users/&#91;username&#93;/Library/Application Support/Adobe/Adobe Substance 3D Designer</td>
</tr><tr><td style="text-align: left;"><b>11.1</b> or lower<br/>
</td>
<td colspan="2" style="text-align: left;">/Users/&#91;username&#93;/Library/Application Support/Allegorithmic/Substance Designer</td>
</tr><tr><td rowspan="2" style="text-align: left;"><b>Linux</b></td>
<td style="text-align: left;"><b>11.2</b> or higher</td>
<td colspan="2" style="text-align: left;">/home/&#91;username&#93;/.local/share/Adobe/Adobe Substance 3D Designer</td>
</tr><tr><td style="text-align: left;"><b>11.1</b> or lower<br/>
</td>
<td colspan="2" style="text-align: left;">/home/&#91;username&#93;/.local/share/Allegorithmic/Substance Designer</td>
</tr></tbody></table>

>[!NOTE]
>
> Some of the directories in the paths mentioned above may be hidden by default. Type the path manually in the file explorer or display hidden files to view them.

>[!IMPORTANT]
>
> Make sure that the file is called **license.key** otherwise the application will not be able to find it.

### ENVIRONMENT VARIABLE

You can override the location that Designer checks for the <b>license.key</b> file with an [environment variable](../../pipeline-and-project-con/environment-variables/environment-variables.md).
