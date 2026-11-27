# Taxonomy overview

The taxonomy characterises the **differences between versions of a tabular dataset** that may affect the ML pipelines that use it. It is organised im the following four **Dimensions**:

- **Metadata**: information that describes the dataset as a whole. 
- **Schema**: which columns exist and what characteristics they have.
- **Instances**: which rows are included and which values they hold.
- **Storage**: how the data are physically stored.

Dimensions are divided into **categories** (for example *Columns set*), that can be also divided into **sub-categories** (*Columns order* or *Column*). The concrete categories (not being decomposed, for example *Columns order*) has its own page describing the category.

<!-- BEGIN GENERATED:tree -->


```mermaid
flowchart LR
    root(["Dataset differences"])
    n0["Related information"]
    root --> n0
    n1["External-related information"]
    n0 --> n1
    n32["Internal-related information"]
    n0 --> n32
    n2["Schema"]
    root --> n2
    n3["Columns set"]
    n2 --> n3
    n4["Columns order"]
    n3 --> n4
    n5["Column"]
    n3 --> n5
    n6["Extra column"]
    n5 --> n6
    n7["Absent column"]
    n5 --> n7
    n8["Rename column"]
    n5 --> n8
    n9["Column characteristics"]
    n2 --> n9
    n10["Categorical"]
    n9 --> n10
    n11["Categorical column type"]
    n10 --> n11
    n12["Categorical column values"]
    n10 --> n12
    n13["Numerical"]
    n9 --> n13
    n14["Numerical column type"]
    n13 --> n14
    n15["Numerical column values"]
    n13 --> n15
    n16["Numerical column format"]
    n13 --> n16
    n17["Instances"]
    root --> n17
    n18["Rows set"]
    n17 --> n18
    n19["Rows order"]
    n18 --> n19
    n20["Row"]
    n18 --> n20
    n21["Extra row"]
    n20 --> n21
    n22["Absent row"]
    n20 --> n22
    n23["Data value"]
    n17 --> n23
    n24["Extra missing"]
    n23 --> n24
    n25["Absent missing"]
    n23 --> n25
    n26["Value update not involving missing"]
    n23 --> n26
    n27["Storage"]
    root --> n27
    n28["Format"]
    n27 --> n28
    n29["Fragmentation"]
    n27 --> n29
    n30["Horizontal"]
    n29 --> n30
    n31["Vertical"]
    n29 --> n31
```
<!-- END GENERATED:tree -->

## How each page is organised

- **Dimension and intermediate category pages** define what they cover and list what they contain.
- **Concrete category pages (leaves)** provide the difference *categoty description*, the *examples of possible implications for the pipeline* and the *typical adaptation*.
