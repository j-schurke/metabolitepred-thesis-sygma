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

    "validate_asp_dipo": pkg_resources.resource_filename('sygma', "rules/validate_Aspirin_ DIPLOSALSALATE.csv"),
    "testRankingSpecific": pkg_resources.resource_filename('sygma', "rules/testRankingSpecific.txt"),
    "testRankingCorrect": pkg_resources.resource_filename('sygma', "rules/testRankingCorrect.txt"),
    "testRankingCorrect_unique": pkg_resources.resource_filename('sygma', "rules/testRankingCorrect_unique_and_unknown.txt"),
    "all_rules_correct0": pkg_resources.resource_filename('sygma', "rules/all_rules_correct0.txt"),
    "all_rules_correct3": pkg_resources.resource_filename('sygma', "rules/all_rules_correct3.txt"),
    "all_rules_specific0": pkg_resources.resource_filename('sygma', "rules/all_rules_specific0.txt"),
    "all_rules_specific3": pkg_resources.resource_filename('sygma', "rules/all_rules_specific3.txt"),
### EC main classes
    "EC1_radius3": pkg_resources.resource_filename('sygma', "rules/all_EC1_3.txt"),
    "EC2_radius3": pkg_resources.resource_filename('sygma', "rules/all_EC2_3.txt"),
    "EC3_radius3": pkg_resources.resource_filename('sygma', "rules/all_EC3_3.txt"),
    "EC4_radius3": pkg_resources.resource_filename('sygma', "rules/all_EC4_3.txt"),
    "EC5_radius3": pkg_resources.resource_filename('sygma', "rules/all_EC5_3.txt"),
    "EC6_radius3": pkg_resources.resource_filename('sygma', "rules/all_EC6_3.txt"),
    "EC7_radius3": pkg_resources.resource_filename('sygma', "rules/all_EC7_3.txt"),
### EC second level
    "EC1.1": pkg_resources.resource_filename('sygma', "rules/all_EC1.1_3.txt"),
    "EC1.2": pkg_resources.resource_filename('sygma', "rules/all_EC1.2_3.txt"),
    "EC1.3": pkg_resources.resource_filename('sygma', "rules/all_EC1.3_3.txt"),
    "EC1.4": pkg_resources.resource_filename('sygma', "rules/all_EC1.4_3.txt"),
    "EC1.5": pkg_resources.resource_filename('sygma', "rules/all_EC1.5_3.txt"),
    "EC1.6": pkg_resources.resource_filename('sygma', "rules/all_EC1.6_3.txt"),
    "EC1.7": pkg_resources.resource_filename('sygma', "rules/all_EC1.7_3.txt"),
    "EC1.8": pkg_resources.resource_filename('sygma', "rules/all_EC1.8_3.txt"),
    "EC1.9": pkg_resources.resource_filename('sygma', "rules/all_EC1.9_3.txt"),

    "EC2.1": pkg_resources.resource_filename('sygma', "rules/all_EC2.1_3.txt"),
    "EC2.2": pkg_resources.resource_filename('sygma', "rules/all_EC2.2_3.txt"),
    "EC2.3": pkg_resources.resource_filename('sygma', "rules/all_EC2.3_3.txt"),
    "EC2.4": pkg_resources.resource_filename('sygma', "rules/all_EC2.4_3.txt"),
    "EC2.5": pkg_resources.resource_filename('sygma', "rules/all_EC2.5_3.txt"),
    "EC2.6": pkg_resources.resource_filename('sygma', "rules/all_EC2.6_3.txt"),
    "EC2.7": pkg_resources.resource_filename('sygma', "rules/all_EC2.7_3.txt"),
    "EC2.8": pkg_resources.resource_filename('sygma', "rules/all_EC2.8_3.txt"),
    "EC2.9": pkg_resources.resource_filename('sygma', "rules/all_EC2.9_3.txt"),

    "EC3.1": pkg_resources.resource_filename('sygma', "rules/all_EC3.1_3.txt"),
    "EC3.2": pkg_resources.resource_filename('sygma', "rules/all_EC3.2_3.txt"),
    "EC3.3": pkg_resources.resource_filename('sygma', "rules/all_EC3.3_3.txt"),
    "EC3.4": pkg_resources.resource_filename('sygma', "rules/all_EC3.4_3.txt"),
    "EC3.5": pkg_resources.resource_filename('sygma', "rules/all_EC3.5_3.txt"),
    "EC3.6": pkg_resources.resource_filename('sygma', "rules/all_EC3.6_3.txt"),
    "EC3.7": pkg_resources.resource_filename('sygma', "rules/all_EC3.7_3.txt"),
    "EC3.8": pkg_resources.resource_filename('sygma', "rules/all_EC3.8_3.txt"),
    "EC3.9": pkg_resources.resource_filename('sygma', "rules/all_EC3.9_3.txt"),

    "EC4.1": pkg_resources.resource_filename('sygma', "rules/all_EC4.1_3.txt"),
    "EC4.2": pkg_resources.resource_filename('sygma', "rules/all_EC4.2_3.txt"),
    "EC4.3": pkg_resources.resource_filename('sygma', "rules/all_EC4.3_3.txt"),
    "EC4.4": pkg_resources.resource_filename('sygma', "rules/all_EC4.4_3.txt"),
    "EC4.5": pkg_resources.resource_filename('sygma', "rules/all_EC4.5_3.txt"),
    "EC4.6": pkg_resources.resource_filename('sygma', "rules/all_EC4.6_3.txt"),
    "EC4.7": pkg_resources.resource_filename('sygma', "rules/all_EC4.7_3.txt"),
    "EC4.8": pkg_resources.resource_filename('sygma', "rules/all_EC4.8_3.txt"),
    "EC4.9": pkg_resources.resource_filename('sygma', "rules/all_EC4.9_3.txt"),

    "EC6.1": pkg_resources.resource_filename('sygma', "rules/all_EC6.1_3.txt"),
    "EC4.2": pkg_resources.resource_filename('sygma', "rules/all_EC6.2_3.txt"),
    "EC6.3": pkg_resources.resource_filename('sygma', "rules/all_EC6.3_3.txt"),
    "EC6.4": pkg_resources.resource_filename('sygma', "rules/all_EC6.4_3.txt"),
    "EC6.5": pkg_resources.resource_filename('sygma', "rules/all_EC6.5_3.txt"),
    "EC6.6": pkg_resources.resource_filename('sygma', "rules/all_EC6.6_3.txt"),
    "EC6.7": pkg_resources.resource_filename('sygma', "rules/all_EC6.7_3.txt"),


}
