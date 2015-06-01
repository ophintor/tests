import re
def format_patch_list(patches_list):
    """
    This function extracts the list of one-off patches applied to the system
    and returns it separated by commas, so it can be easily used to do a
    rollback of multiple patches by using opatch nrollback
    """

    patches_formatted_list = []
    for p in patches_list.splitlines():
        if p:
            pnum = p.split(';')[0]
            if len(p.split(';'))>1:
                desc = p.split(';')[1]
            else:
                desc = ""

            if not desc or re.search("Oracle JAVAVM COMPONENT", desc, re.IGNORECASE):
                patches_formatted_list.append(pnum)

    return ','.join(patches_formatted_list)



patches = """
19877443;1234 ORACLE JAVAVM COMPONENT blablabla
19718130;
19686963;
17991041;
17508816;
17063116;
14764540;
14742362;
14237433;
14009271;
13940331;
13879553;
13846587;
13514126;
13501787;
13494030;
13355095;
13040331;
10190759;
19769496;Database Patch Set Update : 11.2.0.3.13 (19769496)
"""

one_off_patches=format_patch_list(patches)
print one_off_patches