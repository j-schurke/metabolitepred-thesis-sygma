"""
SyGMa comes currently with two rulesets:

phase1
    Phase 1 metabolism rules include mainly different types of oxidation, hydrolysis, reduction
    and condensation reactions

phase2
    Phase 2 metabolism rules include severaly conjugation reaction,
    i.e. with glucuronyl, sulfate, methyl and acetyl
"""
import pkg_resources

ruleset = {
    "phase1": pkg_resources.resource_filename('sygma', "rules/phase1.txt"),
    "phase2": pkg_resources.resource_filename('sygma', "rules/phase2.txt"),
    "phase3": pkg_resources.resource_filename('sygma', "rules/phase3.txt"),

    "ecocyc_0": pkg_resources.resource_filename('sygma', "rules/ecocyc_0.csv"),
    "kegg_reaction_0": pkg_resources.resource_filename('sygma', "rules/kegg_reaction_0.csv"),
    "macie_0": pkg_resources.resource_filename('sygma', "rules/macie_0.csv"),
    "metacyc_0": pkg_resources.resource_filename('sygma', "rules/metacyc_0.csv"),
    "reactome_0": pkg_resources.resource_filename('sygma', "rules/reactome_0.csv"),
    "rhea_0": pkg_resources.resource_filename('sygma', "rules/rhea_0.csv"),
    "rhea_1": pkg_resources.resource_filename('sygma', "rules/rhea_1.csv"),
    "rhea_2": pkg_resources.resource_filename('sygma', "rules/rhea_2.csv"),
    "rhea_unique_0": pkg_resources.resource_filename('sygma', "rules/rhea_unique_0.csv"),
    "rhea_unique_1": pkg_resources.resource_filename('sygma', "rules/rhea_unique_1.csv"),
    "rhea_unique_2": pkg_resources.resource_filename('sygma', "rules/rhea_unique_2.csv"),

    "tmp": pkg_resources.resource_filename('sygma', "rules/tmp.csv"),

    "chembl_0": pkg_resources.resource_filename('sygma', "rules/chembl_0.csv"),
    "chembl_1": pkg_resources.resource_filename('sygma', "rules/chembl_1.csv"),
    "chembl_2": pkg_resources.resource_filename('sygma', "rules/chembl_2.csv"),
    "chembl_unique_0": pkg_resources.resource_filename('sygma', "rules/chembl_unique_0.csv"),
    "chembl_unique_1": pkg_resources.resource_filename('sygma', "rules/chembl_unique_1.csv"),
    "chembl_unique_2": pkg_resources.resource_filename('sygma', "rules/chembl_unique_2.csv"),
}
