=======
Inputs
=======

The tool requires either both an APMS edgelist TSV and a baitlist TSV file, detailing gene interactions and targets
respectively, or a single .tsv file from the CM4AI RO-Crate.
Below is the list and description of each input accepted by the tool.

Output files and directories
-----------------------------

- ``baitlist.tsv``
    This file contains information about the bait proteins used in the affinity purification-mass spectrometry (AP-MS) process.

**Example:**

.. code-block::

    GeneSymbol	GeneID	# Interactors
    PIK3CA	101928739	2783

- ``edgelist.tsv``
    An edge list representation of the protein-protein interactions. Each row in this file represents an interaction between two proteins.

**Example:**

.. code-block::

    GeneID1	Symbol1	GeneID2	Symbol2
    101928739	PIK3CA	219541	MED19
    101928739	PIK3CA	26030	PLEKHG3
    101928739	PIK3CA	129446	XIRP2
    101928739	PIK3CA	644815	FAM83G
    101928739	PIK3CA	23347	SMCHD1

- ``CM4AI_TABLE_PATH``:
    A `.tsv` file from CM4AI RO-Crate that should contain at least the following columns: Bait, Prey, logOddsScore, FoldChange.x, and BFDR.x.

**Example:**

.. code-block::

    Bait	Prey	PreyGene.x	Spec	SpecSum	AvgSpec	NumReplicates.x	ctrlCounts	AvgP.x	MaxP.x	TopoAvgP.x	TopoMaxP.x	SaintScore.x	logOddsScore	FoldChange.x	BFDR.x	boosted_by.x
    DNMT3A	O00422	SAP18_HUMAN	6|7|8|10	31	7.75	4	0|0|0|0|0|0|0|0	1.0	1.0	1.0	1.0	1.0	13.51	77.5	0.0
    DNMT3A	O00571	DDX3X_HUMAN	3|7|11|9	30	7.5	4	0|1|3|3|0|0|0|0	0.99	1.0	0.99	1.0	0.99	3.63	8.57	0.0
    DNMT3A	O15027	SC16A_HUMAN	40|38|32|37	147	36.75	4	0|0|0|0|0|0|0|0	1.0	1.0	1.0	1.0	1.0	52.31	367.5	0.0
    DNMT3A	O15042	SR140_HUMAN	5|3|4|2	14	3.5	4	2|0|2|2|0|0|0|0	0.98	1.0	0.98	1.0	0.98	2.81	4.67	0.0
    DNMT3A	O15056	SYNJ2_HUMAN	5|6|7|5	23	5.75	4	0|0|0|0|0|0|0|0	1.0	1.0	1.0	1.0	1.0	11.87	57.5	0.0
    DNMT3A	O43143	DHX15_HUMAN	8|13|9|16	46	11.5	4	0|0|1|0|0|0|0|0	1.0	1.0	1.0	1.0	1.0	16.2	92.0	0.0


- ``provenance.json``
    Path to file containing provenance information about input files in JSON format.
    This is required and not including will output error message with example of file.

**Example:**

.. code-block::

    {
      "name": "Example input dataset",
      "organization-name": "CM4AI",
      "project-name": "Example",
      "edgelist": {
        "name": "Antoine Forget sample edgelist",
        "author": "Krogan Lab",
        "version": "1.0",
        "date-published": "07-31-2023",
        "description": "AP-MS Protein interactions on HSC2 cell line, example dataset",
        "data-format": "tsv"
      },
      "baitlist": {
        "name": "Antoine Forget sample baitlist",
        "author": "Krogan Lab",
        "version": "1.0",
        "date-published": "07-31-2023",
        "description": "AP-MS Baits used for Protein interactions on HSC2 cell line",
        "data-format": "tsv"
      },
      "samples": {
        "name": "u2os HPA IF images",
        "author": "Author of dataset",
        "version": "Version of dataset",
        "date-published": "Date dataset was published",
        "description": "Description of dataset",
        "data-format": "csv"
      },
      "unique": {
        "name": "u2os HPA IF images unique",
        "author": "Author of dataset",
        "version": "Version of dataset",
        "date-published": "Date dataset was published",
        "description": "Description of dataset",
        "data-format": "csv"
      }
    }



