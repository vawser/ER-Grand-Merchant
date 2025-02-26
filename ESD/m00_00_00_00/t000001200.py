# -*- coding: utf-8 -*-
def t000001200_1():
    """State 0,1"""
    # actionbutton:6210:"Talk"
    t000001200_x5(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z8=1, z9=1000000, z10=1000000,
                  z11=1000000, mode1=1, mode2=1)
    Quit()

def t000001200_1000():
    """State 0,2,3"""
    assert t000001200_x35()
    """State 1"""
    c1_120(1000)
    Quit()

def t000001200_2000():
    """State 0,2,3"""
    assert t000001200_x36()
    """State 1"""
    c1_120(2000)
    Quit()

def t000001200_x0(actionbutton1=6210, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                  flag4=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag5) == 1 or GetEventFlag(flag9) == 1 or GetEventFlag(flag10) == 1 or
                GetEventFlag(flag11) == 1 or GetEventFlag(flag12) == 1)
        """State 4"""
        assert not GetEventFlag(flag4)
        """State 2"""
        if GetEventFlag(flag4) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag5) and not GetEventFlag(flag9) and not GetEventFlag(flag10) and not
              GetEventFlag(flag11) and not GetEventFlag(flag12)):
            pass
        # actionbutton:6210:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t000001200_x1():
    """State 0,1"""
    if not CheckSpecificPersonTalkHasEnded(0):
        """State 7"""
        ClearTalkProgressData()
        StopEventAnimWithoutForcingConversationEnd(0)
        """State 6"""
        ReportConversationEndToHavokBehavior()
    else:
        pass
    """State 2"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 3"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 4"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 5"""
        ForceCloseMenu()
    else:
        pass
    """State 8"""
    return 0

def t000001200_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t000001200_x3(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t000001200_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t000001200_x1()
    else:
        """State 4,7"""
        call = t000001200_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t000001200_x1()
    """State 9"""
    return 0

def t000001200_x4():
    """State 0,1"""
    assert t000001200_x1()
    """State 2"""
    return 0

def t000001200_x5(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z8=1, z9=1000000, z10=1000000,
                  z11=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t000001200_x22(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z8=z8, z9=z9, z10=z10, z11=z11,
                              mode1=mode1, mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t000001200_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t000001200_x6(val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z8=1, z9=1000000, z10=1000000, z11=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t000001200_x9(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z9=z9, z10=z10, z11=z11)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t000001200_x13(val1=val1, z8=z8)
            def WhilePaused():
                c5_138(GetDistanceToPlayer() > 2.5, -1)
                RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
                GiveSpEffectToPlayer(9640)
                c5_139(1 == (mode1 == 1), -1, 0)
                c5_139(1 == (mode2 == 1), 0, -1)
            def ExitPause():
                c1_138(-1)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif IsAttackedBySomeone() == 1 and not DoesSelfHaveSpEffect(9626) and not DoesSelfHaveSpEffect(9627):
            pass
        elif GetEventFlag(flag8) == 1:
            Goto('L0')
        elif GetEventFlag(flag6) == 1 and not GetEventFlag(flag7) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t000001200_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t000001200_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t000001200_x11(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t000001200_x7(val2=10, val3=12):
    """State 0,1"""
    call = t000001200_x17(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t000001200_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t000001200_x8(flag1=3223, val2=10, val3=12):
    """State 0,8"""
    assert t000001200_x34()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t000001200_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t000001200_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t000001200_x9(actionbutton1=6210, flag4=6000, flag5=6001, z9=1000000, z10=1000000, z11=1000000):
    """State 0,1"""
    call = t000001200_x10(z17=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t000001200_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001200_x10(z17=_, val6=_):
    """State 0,1"""
    if f203(z17) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z17)
        assert f202() == val6
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t000001200_x11(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t000001200_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t000001200_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t000001200_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t000001200_x12():
    """State 0,1"""
    assert t000001200_x10(z17=1101, val6=1101)
    """State 2"""
    return 0

def t000001200_x13(val1=5, z8=1):
    """State 0,2"""
    assert t000001200_x23()
    """State 1"""
    call = t000001200_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t000001200_x25()
    """State 4"""
    return 0

def t000001200_x14():
    """State 0,1"""
    assert t000001200_x10(z17=1000, val6=1000)
    """State 2"""
    return 0

def t000001200_x15(val5=30):
    """State 0,1"""
    call = t000001200_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t000001200_x26()
    """State 3"""
    return 0

def t000001200_x16():
    """State 0,1"""
    assert t000001200_x10(z17=1100, val6=1100)
    """State 2"""
    return 0

def t000001200_x17(val2=10, val3=12):
    """State 0,5"""
    assert t000001200_x34()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t000001200_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t000001200_x28()
    """Unused"""
    """State 6"""
    return 0

def t000001200_x18():
    """State 0,2"""
    call = t000001200_x10(z17=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t000001200_x19():
    """State 0,1"""
    assert t000001200_x10(z17=1001, val6=1001)
    """State 2"""
    return 0

def t000001200_x20():
    """State 0,1"""
    assert t000001200_x10(z17=1103, val6=1103)
    """State 2"""
    return 0

def t000001200_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t000001200_x22(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z8=1, z9=1000000, z10=1000000,
                   z11=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t000001200_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z8=z8,
                             z9=z9, z10=z10, z11=z11, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t000001200_x8(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t000001200_x7(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t000001200_x33() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t000001200_x23():
    """State 0,1"""
    assert t000001200_x24()
    """State 2"""
    return 0

def t000001200_x24():
    """State 0,1"""
    assert t000001200_x10(z17=1104, val6=1104)
    """State 2"""
    return 0

def t000001200_x25():
    """State 0,1"""
    call = t000001200_x10(z17=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t000001200_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001200_x26():
    """State 0,1"""
    call = t000001200_x10(z17=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t000001200_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001200_x27():
    """State 0,1"""
    call = t000001200_x10(z17=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t000001200_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001200_x28():
    """State 0,1"""
    call = t000001200_x10(z17=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t000001200_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001200_x29(z15=_, z16=_):
    """State 0,4"""
    assert t000001200_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(z15, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not z16:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t000001200_x30(z12=_, z13=_, z14=_):
    """State 0,5"""
    assert t000001200_x31() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(z13, 1)
    """State 1"""
    TalkToPlayer(z12, -1, -1, 1)
    """State 4"""
    if not z14:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t000001200_x31():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t000001200_x32():
    """State 0,1"""
    assert t000001200_x10(z17=1002, val6=1002)
    """State 2"""
    return 0

def t000001200_x33():
    """State 0,1"""
    assert t000001200_x1()
    """State 2"""
    return 0

def t000001200_x34():
    """State 0,1"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 2"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 3"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 4"""
        ForceCloseMenu()
    else:
        pass
    """State 5"""
    return 0

def t000001200_x35():
    """State 0"""
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 8"""
    assert t000001200_x38()
    """State 9"""
    return 0

def t000001200_x36():
    """State 0,1"""
    # actionbutton:6210:"Talk"
    assert (t000001200_x0(actionbutton1=6210, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
            flag4=6000))
    """State 4"""
    return 0

# Main Menu
def t000001200_x38():
    c1_110()
    while True:
        ClearTalkListData()
        
        # Access Grand Repository
        AddTalkListData(1, 99999300, -1)
        
        # Level Up
        AddTalkListData(3, 15000540, -1)
        
        # Memorize spell
        AddTalkListData(4, 15000390, -1)
        
        # Ashes of War
        AddTalkListData(8, 15000530, -1)
        
        # Leave
        AddTalkListData(99, 20000009, -1)
        
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Access Grand Repository
        if GetTalkListEntryResult() == 1:
            assert t000001200_x100()
        # Level Up
        elif GetTalkListEntryResult() == 3:
            OpenSoul()
            assert not (CheckSpecificPersonMenuIsOpen(10, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Memorize spell
        elif GetTalkListEntryResult() == 4:
            OpenMagicEquip(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(11, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Ashes of War
        elif GetTalkListEntryResult() == 8:
            OpenEquipmentChangeOfPurposeShop()
            assert not (CheckSpecificPersonMenuIsOpen(7, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        else:
            return 0
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    return 0

# Access Grand Repository
def t000001200_x100():
    """State 0"""
    c1_110()
    ClearTalkActionState()
    while True:
        """State 2"""
        ClearTalkListData()
        
        # Browse Inventory
        AddTalkListData(10, 99999030, -1)
        
        # Browse Playthrough Options
        AddTalkListData(2, 99999400, -1)
        
        # Browse Cut Content
        AddTalkListData(11, 99999032, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 1"""
        
        # Browse Inventory
        if GetTalkListEntryResult() == 10:
            """State 32"""
            assert t000001200_x101()
        # Browse Cut Content
        elif GetTalkListEntryResult() == 11:
            """State 33"""
            assert t000001200_x200()
        # Quick Start Options
        elif GetTalkListEntryResult() == 2:
            assert t000001200_x400()
        else:
            """State 12"""
            return 0

# Browse Inventory
def t000001200_x101():
    """State 0"""
    c1_110()
    ClearTalkActionState()
    while True:
        """State 2"""
        ClearTalkListData()
        
        # Weapons
        AddTalkListData(1, 99999000, -1)
        
        # Ammunition
        AddTalkListData(2, 99999004, -1)
        
        # Spells
        AddTalkListData(3, 99999002, -1)
        
        # Ashes of War
        AddTalkListData(4, 99999005, -1)
        
        # Armor
        AddTalkListData(5, 99999001, -1)
        
        # Talismans
        AddTalkListData(6, 99999003, -1)
        
        # Items
        AddTalkListData(7, 99999031, -1)
        
        # Gestures
        AddTalkListData(11, 99999010, -1)
        
        # Runes
        AddTalkListData(12, 99999012, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 1"""
        
        # Weapons
        if GetTalkListEntryResult() == 1:
            """State 3"""
            OpenRegularShop(9100000, 9109999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Armor
        elif GetTalkListEntryResult() == 5:
            """State 5"""
            OpenRegularShop(9110000, 9119999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Spells
        elif GetTalkListEntryResult() == 3:
            """State 6"""
            OpenRegularShop(9120000, 9129999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Talismans
        elif GetTalkListEntryResult() == 6:
            """State 7"""
            OpenRegularShop(9130000, 9139999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Ammunition
        elif GetTalkListEntryResult() == 2:
            """State 8"""
            OpenRegularShop(9140000, 9149999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Ashes of War
        elif GetTalkListEntryResult() == 4:
            """State 9"""
            OpenRegularShop(9150000, 9159999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Items
        elif GetTalkListEntryResult() == 7:
            """State 10"""
            assert t000001200_x102()
        # Gestures
        elif GetTalkListEntryResult() == 11:
            """State 11"""
            assert t000001200_x110()
        # Runes
        elif GetTalkListEntryResult() == 12:
            assert t000001200_x312(99999013)
        else:
            """State 12"""
            return 0

# Items
def t000001200_x102():
    """State 0"""
    c1_110()
    ClearTalkActionState()
    while True:
        """State 2"""
        ClearTalkListData()
        
        # Consumables
        AddTalkListData(1, 99999006, -1)
        
        # Materials
        AddTalkListData(2, 99999008, -1)
        
        # Spirit Summons
        AddTalkListData(3, 99999007, -1)
        
        # Miscellaneous Items
        AddTalkListData(4, 99999009, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 1"""
        
        # Consumables
        if GetTalkListEntryResult() == 1:
            """State 3"""
            OpenRegularShop(9170000, 9179999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Materials
        elif GetTalkListEntryResult() == 2:
            """State 5"""
            OpenRegularShop(9180000, 9189999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Spirit Summons
        elif GetTalkListEntryResult() == 3:
            """State 6"""
            OpenRegularShop(9160000, 9169999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Miscellaneous Items
        elif GetTalkListEntryResult() == 4:
            """State 7"""
            OpenRegularShop(9190000, 9199999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        else:
            """State 8"""
            return 0

# Gestures - Valid
def t000001200_x110():
    """State 0"""
    c1_110()
    ClearTalkActionState()
    """State 2"""
    ClearTalkListData()
    
    # Unlock
    AddTalkListData(1, 99999100, -1)
    
    # Leave
    AddTalkListData(9, 20000009, -1)
    """State 4"""
    ShowShopMessage(1)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 1"""
    
    # Unlock
    if GetTalkListEntryResult() == 1:
        assert t000001200_x310(action3=99999700)
        return 0
    else:
        """State 5"""
        return 0

# Browse Cut Content
def t000001200_x200():
    """State 0"""
    c1_110()
    ClearTalkActionState()
    while True:
        """State 2"""
        ClearTalkListData()
        
        # Armor
        AddTalkListData(1, 99999001, -1)
        
        # Talismans
        AddTalkListData(2, 99999003, -1)
        
        # Goods
        AddTalkListData(3, 99999033, -1)
        
        # Gestures
        AddTalkListData(11, 99999010, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 1"""
        # Armor
        if GetTalkListEntryResult() == 1:
            """State 3"""
            OpenRegularShop(9210000, 9219999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Talismans
        elif GetTalkListEntryResult() == 2:
            OpenRegularShop(9220000, 9229999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Goods
        elif GetTalkListEntryResult() == 3:
            """State 5"""
            OpenRegularShop(9200000, 9209999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Gestures
        elif GetTalkListEntryResult() == 11:
            """State 6"""
            assert t000001200_x210()
        else:
            """State 7"""
            return 0

# Gestures - Cut Content
def t000001200_x210():
    """State 0"""
    c1_110()
    ClearTalkActionState()
    """State 2"""
    ClearTalkListData()
    
    # Unlock
    AddTalkListData(1, 99999100, -1)
    
    # Leave
    AddTalkListData(9, 20000009, -1)
    """State 4"""
    ShowShopMessage(1)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 1"""
    
    # Unlock Gestures
    if GetTalkListEntryResult() == 1:
        assert t000001200_x310(action3=99999701)
        return 0
    else:
        """State 5"""
        return 0
        
# Dialog
def t000001200_x301(action1=_):
    """State 0,1"""
    OpenGenericDialog(8, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0
    
# Yes/No prompt
def t000001200_x300(action3=_, z5=_, z6=_):
    """State 0"""
    assert t000001200_x301(action1=action3)
    """State 1"""
    c1_110()
    ClearTalkListData()
    AddTalkListData(1, 99999500, -1)
    AddTalkListData(2, 99999501, -1)
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    if GetTalkListEntryResult() == 1:
        """State 3"""
        SetEventFlag(z5, z6)
        return 0
    elif GetTalkListEntryResult() == 2:
        """State 4"""
        return 1
    else:
        """State 5"""
        return 2
    """Unused"""
    """State 6"""
    return 0
    
# Yes/No prompt - Gestures
def t000001200_x310(action3=_):
    """State 0"""
    assert t000001200_x301(action1=action3)
    """State 1"""
    c1_110()
    ClearTalkListData()
    AddTalkListData(1, 99999500, -1)
    AddTalkListData(2, 99999501, -1)
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    if GetTalkListEntryResult() == 1:
        # gesture:0:Bow
        AcquireGesture(0)
        SetEventFlag(60800, 1)
        # gesture:1:Polite Bow
        AcquireGesture(1)
        SetEventFlag(60801, 1)
        # gesture:2:My Thanks
        AcquireGesture(2)
        SetEventFlag(60802, 1)
        # gesture:3:Curtsy
        AcquireGesture(3)
        SetEventFlag(60803, 1)
        # gesture:4:Reverential Bow
        AcquireGesture(4)
        SetEventFlag(60804, 1)
        # gesture:5:My Lord
        AcquireGesture(5)
        SetEventFlag(60805, 1)
        # gesture:6:Warm Welcome
        AcquireGesture(6)
        SetEventFlag(60806, 1)
        # gesture:7:Wave
        AcquireGesture(7)
        SetEventFlag(60807, 1)
        # gesture:8:Casual Greeting
        AcquireGesture(8)
        SetEventFlag(60808, 1)
        # gesture:9:Strength!
        AcquireGesture(9)
        SetEventFlag(60809, 1)
        # gesture:10:As You Wish
        AcquireGesture(10)
        SetEventFlag(60810, 1)
        # gesture:20:Point Forwards
        AcquireGesture(20)
        SetEventFlag(60811, 1)
        # gesture:21:Point Upwards
        AcquireGesture(21)
        SetEventFlag(60812, 1)
        # gesture:22:Point Downwards
        AcquireGesture(22)
        SetEventFlag(60813, 1)
        # gesture:23:Beckon
        AcquireGesture(23)
        SetEventFlag(60814, 1)
        # gesture:24:Wait!
        AcquireGesture(24)
        SetEventFlag(60815, 1)
        # gesture:25:Calm Down!
        AcquireGesture(25)
        SetEventFlag(60816, 1)
        # gesture:30:Nod In Thought
        AcquireGesture(30)
        SetEventFlag(60817, 1)
        # gesture:40:Extreme Repentance
        AcquireGesture(40)
        SetEventFlag(60818, 1)
        # gesture:41:Grovel For Mercy
        AcquireGesture(41)
        SetEventFlag(60819, 1)
        # gesture:50:Rallying Cry
        AcquireGesture(50)
        SetEventFlag(60820, 1)
        # gesture:51:Heartening Cry
        AcquireGesture(51)
        SetEventFlag(60821, 1)
        # gesture:52:By My Sword
        AcquireGesture(52)
        SetEventFlag(60822, 1)
        # gesture:53:Hoslow's Oath
        AcquireGesture(53)
        SetEventFlag(60823, 1)
        # gesture:54:Fire Spur Me
        AcquireGesture(54)
        SetEventFlag(60824, 1)
        # gesture:60:Bravo!
        AcquireGesture(60)
        SetEventFlag(60826, 1)
        # gesture:70:Jump for Joy
        AcquireGesture(70)
        SetEventFlag(60827, 1)
        # gesture:71:Triumphant Delight
        AcquireGesture(71)
        SetEventFlag(60828, 1)
        # gesture:72:Fancy Spin
        AcquireGesture(72)
        SetEventFlag(60829, 1)
        # gesture:73:Finger Snap
        AcquireGesture(73)
        SetEventFlag(60830, 1)
        # gesture:80:Dejection
        AcquireGesture(80)
        SetEventFlag(60831, 1)
        # gesture:90:Patches' Crouch
        AcquireGesture(90)
        SetEventFlag(60832, 1)
        # gesture:91:Crossed Legs
        AcquireGesture(91)
        SetEventFlag(60833, 1)
        # gesture:92:Rest
        AcquireGesture(92)
        SetEventFlag(60834, 1)
        # gesture:93:Sitting Sideways
        AcquireGesture(93)
        SetEventFlag(60835, 1)
        # gesture:94:Dozing Cross-Legged
        AcquireGesture(94)
        SetEventFlag(60836, 1)
        # gesture:95:Spread Out
        AcquireGesture(95)
        SetEventFlag(60837, 1)
        # gesture:97:Balled Up
        AcquireGesture(97)
        SetEventFlag(60839, 1)
        # gesture:98:What Do You Want?
        AcquireGesture(98)
        SetEventFlag(60840, 1)
        # gesture:100:Prayer
        AcquireGesture(100)
        SetEventFlag(60841, 1)
        # gesture:101:Desperate Prayer
        AcquireGesture(101)
        SetEventFlag(60842, 1)
        # gesture:102:Rapture
        AcquireGesture(102)
        SetEventFlag(60843, 1)
        SetEventFlag(60844, 1)
        # gesture:103:Erudition
        AcquireGesture(103)
        SetEventFlag(60845, 1)
        # gesture:104:Outer Order
        AcquireGesture(104)
        SetEventFlag(60846, 1)
        # gesture:105:Inner Order
        AcquireGesture(105)
        SetEventFlag(60847, 1)
        # gesture:106:Golden Order Totality
        AcquireGesture(106)
        SetEventFlag(60848, 1)
        # gesture:108:The Ring
        AcquireGesture(108)
        SetEventFlag(60849, 1)
        OpenGenericDialog(7, 99999011, 1, 0, 1)
        return 0
    elif GetTalkListEntryResult() == 2:
        """State 4"""
        return 1
    else:
        """State 5"""
        return 2
    """Unused"""
    """State 6"""
    return 0
    
    # Yes/No prompt - Cut Content Gestures
def t000001200_x311(action3=_):
    """State 0"""
    assert t000001200_x301(action1=action3)
    """State 1"""
    c1_110()
    ClearTalkListData()
    AddTalkListData(1, 99999500, -1)
    AddTalkListData(2, 99999501, -1)
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    if GetTalkListEntryResult() == 1:
        # gesture:55:The Carian Oath
        AcquireGesture(55)
        SetEventFlag(60825, 1)
        # gesture:96:Fetal Position
        AcquireGesture(96)
        SetEventFlag(60838, 1)
        OpenGenericDialog(7, 99999011, 1, 0, 1)
        return 0
    elif GetTalkListEntryResult() == 2:
        """State 4"""
        return 1
    else:
        """State 5"""
        return 2
    """Unused"""
    """State 6"""
    return 0
    
    # Yes/No prompt - Max Runes
def t000001200_x312(action3=_):
    """State 0"""
    assert t000001200_x301(action1=action3)
    """State 1"""
    c1_110()
    ClearTalkListData()
    AddTalkListData(1, 99999500, -1)
    AddTalkListData(2, 99999501, -1)
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    if GetTalkListEntryResult() == 1:
        GiveSpEffectToPlayer(8000000)
        return 0
    elif GetTalkListEntryResult() == 2:
        """State 4"""
        return 1
    else:
        """State 5"""
        return 2
    return 0

# Browse Playthrough Options
def t000001200_x400():
    """State 0"""
    c1_110()
    ClearTalkActionState()
    while True:
        """State 2"""
        ClearTalkListData()
        
        # Progression Unlocks
        AddTalkListData(1, 99999401, -1)
        
        # Teleports
        AddTalkListData(2, 99999402, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 1"""
        
        # Progression Options
        if GetTalkListEntryResult() == 1:
            assert t000001200_x401()
        # Start Location Options
        elif GetTalkListEntryResult() == 2:
            assert t000001200_x402()
        else:
            """State 12"""
            return 0
    
# Progression Unlocks
def t000001200_x401():
    """State 0"""
    c1_110()
    ClearTalkActionState()
    while True:
        """State 2"""
        ClearTalkListData()
        
        # Unlock Complete Map Visibility
        AddTalkListDataIf(GetEventFlag(1047610172) == 0, 1, 99999412, -1)
        
        # Unlock Access to Roundtable Hold
        AddTalkListDataIf(GetEventFlag(1047610171) == 0, 2, 99999411, -1)
        
        # Unlock Torrent
        AddTalkListDataIf(GetEventFlag(1047610170) == 0, 3, 99999410, -1)
        
        # Unlock Flasks
        AddTalkListDataIf(GetEventFlag(1047610300) == 0, 10, 99999420, -1)
        # Unlock Crafting Kit
        AddTalkListDataIf(GetEventFlag(1047610301) == 0, 11, 99999421, -1)
        # Unlock Flask of Wondrous Physick
        AddTalkListDataIf(GetEventFlag(1047610302) == 0, 12, 99999422, -1)
        # Unlock Whetstone Knife
        AddTalkListDataIf(GetEventFlag(1047610303) == 0, 13, 99999423, -1)
        # Unlock Spirit Calling Bell
        AddTalkListDataIf(GetEventFlag(1047610304) == 0, 14, 99999424, -1)
        # Unlock Tailoring Tools
        AddTalkListDataIf(GetEventFlag(1047610305) == 0, 15, 99999425, -1)
        # Unlock Golden Tailoring Tools
        AddTalkListDataIf(GetEventFlag(1047610306) == 0, 16, 99999426, -1)
        
        # Unlock Talisman Pouches
        AddTalkListDataIf(GetEventFlag(1047610310) == 0, 20, 99999430, -1)
        # Unlock Memory Stones
        AddTalkListDataIf(GetEventFlag(1047610311) == 0, 21, 99999431, -1)
        # Unlock Cracked Pots
        AddTalkListDataIf(GetEventFlag(1047610312) == 0, 22, 99999432, -1)
        # Unlock Ritual Pots
        AddTalkListDataIf(GetEventFlag(1047610313) == 0, 23, 99999433, -1)
        # Unlock Perfume Bottles
        AddTalkListDataIf(GetEventFlag(1047610314) == 0, 24, 99999434, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 1"""
        
        # Unlock Complete Map Visibility
        if GetTalkListEntryResult() == 1:
            assert t000001200_x300(action3=99999602, z5=1047610162, z6=1)
            return 0
        # Unlock Access to Roundtable Hold
        elif GetTalkListEntryResult() == 2:
            assert t000001200_x300(action3=99999601, z5=1047610161, z6=1)
            return 0
        # Unlock Access to Torrent
        elif GetTalkListEntryResult() == 3:
            assert t000001200_x300(action3=99999600, z5=1047610160, z6=1)
            return 0
        # Unlock Flasks
        elif GetTalkListEntryResult() == 10:
            assert t000001200_x300(action3=99999810, z5=1047610200, z6=1)
            return 0
        # Unlock Crafting Kit
        elif GetTalkListEntryResult() == 11:
            assert t000001200_x300(action3=99999811, z5=1047610201, z6=1)
            return 0
        # Unlock Flask of Wondrous Physick
        elif GetTalkListEntryResult() == 12:
            assert t000001200_x300(action3=99999812, z5=1047610202, z6=1)
            return 0
        # Unlock Whetstone Knife
        elif GetTalkListEntryResult() == 13:
            assert t000001200_x300(action3=99999813, z5=1047610203, z6=1)
            return 0
        # Unlock Spirit Calling Bell
        elif GetTalkListEntryResult() == 14:
            assert t000001200_x300(action3=99999814, z5=1047610204, z6=1)
            return 0
        # Unlock Tailoring Tools
        elif GetTalkListEntryResult() == 15:
            assert t000001200_x300(action3=99999815, z5=1047610205, z6=1)
            return 0
        # Unlock Golden Tailoring Tools
        elif GetTalkListEntryResult() == 16:
            assert t000001200_x300(action3=99999816, z5=1047610206, z6=1)
            return 0
        # Unlock Talisman Pouches
        elif GetTalkListEntryResult() == 20:
            assert t000001200_x300(action3=99999800, z5=1047610210, z6=1)
            return 0
        # Unlock Memory Stones
        elif GetTalkListEntryResult() == 21:
            assert t000001200_x300(action3=99999801, z5=1047610211, z6=1)
            return 0
        # Unlock Cracked Pots
        elif GetTalkListEntryResult() == 22:
            assert t000001200_x300(action3=99999802, z5=1047610212, z6=1)
            return 0
        # Unlock Ritual Pots
        elif GetTalkListEntryResult() == 23:
            assert t000001200_x300(action3=99999803, z5=1047610213, z6=1)
            return 0
        # Unlock Perfume Bottles
        elif GetTalkListEntryResult() == 24:
            assert t000001200_x300(action3=99999804, z5=1047610214, z6=1)
            return 0
        else:
            """State 12"""
            return 0
            
# Teleports
def t000001200_x402():
    """State 0"""
    c1_110()
    ClearTalkActionState()
    while True:
        """State 2"""
        ClearTalkListData()

        # Teleport to Church of Elleh
        AddTalkListData(1, 99999441, -1)
        
        # Teleport to Mohgwyn Palace
        AddTalkListData(2, 99999440, -1)
        
        # Teleport to Stormveil Castle
        AddTalkListData(3, 99999442, -1)
        
        # Teleport to Leyndell, Royal Capital
        AddTalkListData(4, 99999443, -1)
        
        # Teleport to Miquella's Haligtree
        AddTalkListData(5, 99999444, -1)
        
        # Teleport to Crumbling Farum Azula
        AddTalkListData(6, 99999445, -1)
        
        # Teleport to Academy of Raya Lucaria
        AddTalkListData(7, 99999446, -1)
        
        # Teleport to Volcano Manor
        AddTalkListData(8, 99999447, -1)
        
        # Teleport to Redmane Castle
        AddTalkListData(9, 99999448, -1)
        
        # Teleport to Consecrated Snowfield
        AddTalkListData(10, 99999449, -1)
        
        # Teleport to Teleport to Mountaintops of the Giants
        AddTalkListData(11, 99999450, -1)
        
        # Leave
        AddTalkListData(99, 20000009, -1)
        
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 1"""
        
        # Teleport to Church of Elleh
        if GetTalkListEntryResult() == 1:
            assert t000001200_x300(action3=99999611, z5=1047610400, z6=1)
        # Teleport to Mohgwyn Palace
        elif GetTalkListEntryResult() == 2:
            assert t000001200_x300(action3=99999610, z5=1047610401, z6=1)
        # Teleport to Stormveil Castle
        elif GetTalkListEntryResult() == 3:
            assert t000001200_x300(action3=99999612, z5=1047610402, z6=1)
        # Teleport to Leyndell, Royal Capital
        elif GetTalkListEntryResult() == 4:
            assert t000001200_x300(action3=99999613, z5=1047610403, z6=1)
        # Teleport to Miquella's Haligtree
        elif GetTalkListEntryResult() == 5:
            assert t000001200_x300(action3=99999614, z5=1047610404, z6=1)
        # Teleport to Crumbling Farum Azula
        elif GetTalkListEntryResult() == 6:
            assert t000001200_x300(action3=99999615, z5=1047610405, z6=1)
        # Teleport to Academy of Raya Lucaria
        elif GetTalkListEntryResult() == 7:
            assert t000001200_x300(action3=99999616, z5=1047610406, z6=1)
        # Teleport to Volcano Manor
        elif GetTalkListEntryResult() == 8:
            assert t000001200_x300(action3=99999617, z5=1047610407, z6=1)
        # Teleport to Redmane Castle
        elif GetTalkListEntryResult() == 9:
            assert t000001200_x300(action3=99999618, z5=1047610408, z6=1)
        # Teleport to Consecrated Snowfield
        elif GetTalkListEntryResult() == 10:
            assert t000001200_x300(action3=99999619, z5=1047610409, z6=1)
        # Teleport to Mountaintops of the Giants
        elif GetTalkListEntryResult() == 11:
            assert t000001200_x300(action3=99999620, z5=1047610410, z6=1)
        else:
            """State 12"""
            return 0
            