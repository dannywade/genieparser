expected_output ={
    "lentry_label": {
        24: {
            "aal": {
                "deagg_vrf_id": 0,
                "eos0": {"adj_hdl": "0xf9000002", "hw_hdl": "0x7f02737e2ca8"},
                "eos1": {"adj_hdl": "0xf9000002", "hw_hdl": "0x7f02737e2a98"},
                "id": 1996488716,
                "lbl": 24,
                "lspa_handle": "0",
            },
            "adj": {
                109: {
                    "adj": "0xdf000026",
                    "ifnum": "0x33",
                    "link_type": "MPLS",
                    "si": "0x7f0273423ab8",
                },
                139: {
                    "adj": "0x5c000037",
                    "ifnum": "0x36",
                    "link_type": "MPLS",
                    "si": "0x7f02737a2348",
                },
            },
            "backwalk_cnt": 0,
            "label": {
                31: {
                    "adj_handle": "0x62000061",
                    "bwalk_cnt": 0,
                    "collapsed_oce": 0,
                    "flags": {"0x1": ["REAL"]},
                    "label_aal": {
                        1644167265: {
                            "adj_flags": "0",
                            "di_id": "0x526d",
                            "dmac": "0027.90bf.2ee7",
                            "label_type": 2,
                            "lbl": 0,
                            "link_type": 2,
                            "phdl": "0xab000447",
                            "ref_cnt": 1,
                            "rewrite_type": "PSH1(119)",
                            "ri": "0x7f02737e8a98",
                            "ri_id": "0x4e",
                            "si": "0x7f02737c1b08",
                            "si_id": "0x4034",
                            "smac": "00a7.42d6.c41f",
                            "sub_type": 0,
                            "vlan_id": 0,
                            "vrf_id": 0,
                        }
                    },
                    "link_type": "MPLS",
                    "local_adj": 0,
                    "local_label": 24,
                    "modify_cnt": 0,
                    "olbl_changed": 0,
                    "outlabel": "(34, 0)",
                    "pdflags": {"0": ["INSTALL_HW_OK"]},
                    "subwalk_cnt": 0,
                    "unsupported_recursion": 0,
                },
                32: {
                    "adj_handle": "0x89000062",
                    "bwalk_cnt": 0,
                    "collapsed_oce": 0,
                    "flags": {"0x1": ["REAL"]},
                    "label_aal": {
                        2298478690: {
                            "adj_flags": "0",
                            "di_id": "0x5268",
                            "dmac": "00a7.42ce.f69f",
                            "label_type": 2,
                            "lbl": 0,
                            "link_type": 2,
                            "phdl": "0x7c000442",
                            "ref_cnt": 1,
                            "rewrite_type": "PSH1(119)",
                            "ri": "0x7f027379b138",
                            "ri_id": "0x24",
                            "si": "0x7f02737a4d58",
                            "si_id": "0x4035",
                            "smac": "00a7.42d6.c41f",
                            "sub_type": 0,
                            "vlan_id": 0,
                            "vrf_id": 0,
                        }
                    },
                    "link_type": "MPLS",
                    "local_adj": 0,
                    "local_label": 24,
                    "modify_cnt": 0,
                    "olbl_changed": 0,
                    "outlabel": "(29, 0)",
                    "pdflags": {"0": ["INSTALL_HW_OK"]},
                    "subwalk_cnt": 0,
                    "unsupported_recursion": 0,
                },
            },
            "lb": {
                38: {
                    "aal": {
                        "af": 0,
                        "ecr_id": 4177526786,
                        "ecr_type": "0",
                        "ecrh": "0x7f02737e49f8(28:2)",
                        "hwhdl": ":1937656312 "
                        "::0x7f02737e11c8,0x7f02737e2728,0x7f02737e11c8,0x7f02737e2728",
                        "ref": 3,
                    },
                    "bwalk": {"in_prog": 0, "nested": 0, "req": 0},
                    "bwalk_cnt": 0,
                    "ecr_map_objid": 0,
                    "ecrh": "0xf9000002",
                    "finish_cnt": 0,
                    "flags": "0",
                    "link_type": "IP",
                    "local_label": 24,
                    "modify_cnt": 0,
                    "mpls_ecr": 1,
                    "num_choices": 2,
                    "old_ecrh": "0",
                    "path_inhw": 2,
                    "subwalk_cnt": 0,
                }
            },
            "lentry_hdl": "0x7700000c",
            "lspa_handle": "0",
            "modify_cnt": 8,
            "nobj": ["LB", " 38"],
            "sw_enh_ecr_scale": {
                38: {
                    "adjs": 2,
                    "ecr_adj": {
                        1644167265: {
                            "adj_lentry": "[eos0:0x7f02734123b8 "
                            "eos1:0x7f02737ec5e8]",
                            "di_id": 20499,
                            "is_mpls_adj": 1,
                            "l3adj_flags": "0x100000",
                            "recirc_adj_id": 3120562239,
                            "rih": "0x7f02737e0bf8(74)",
                            "sih": "0x7f02737e11c8(182)",
                        },
                        2298478690: {
                            "adj_lentry": "[eos0:0x7f02737e6dd8 "
                            "eos1:0x7f02737b21d8]",
                            "di_id": 20499,
                            "is_mpls_adj": 1,
                            "l3adj_flags": "0x100000",
                            "recirc_adj_id": 1442840640,
                            "rih": "0x7f02737dcbe8(75)",
                            "sih": "0x7f02737e2728(183)",
                        },
                        2483028067: {
                            "di_id": 20499,
                            "rih": "0x7f02737eaa18(52)",
                            "sih": "0x7f02737e4c08(170)",
                        },
                    },
                    "ecr_hwhdl": "0x7f02737e49f8",
                    "ecrhdl": "0xf9000002",
                    "eos": 1,
                    "llabel": 24,
                    "mixed_adj": "0",
                    "mod_cnt": 0,
                    "pmismatch": 0,
                    "pordermatch": 0,
                    "prev_npath": 0,
                    "reprogram_hw": "0",
                }
            },
        }
    }
}