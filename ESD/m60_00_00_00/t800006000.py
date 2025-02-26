# -*- coding: utf-8 -*-
def t800006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t800006000_x7(flag1=4703, flag2=4701, flag3=4702, val2=5, val3=10, val4=12, val5=10, val6=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z2=1, z3=1000000, z4=1000000,
                  z5=1000000, mode1=1, mode2=1)
    Quit()

def t800006000_1000():
    """State 0,2,3"""
    assert t800006000_x37()
    """State 1"""
    c1_120(1000)
    Quit()

def t800006000_1001():
    """State 0,2,3"""
    assert t800006000_x38()
    """State 1"""
    c1_120(1001)
    Quit()

def t800006000_1101():
    """State 0,2,3"""
    assert t800006000_x39()
    """State 1"""
    c1_120(1101)
    Quit()

def t800006000_1102():
    """State 0,2,3"""
    t800006000_x40()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t800006000_1103():
    """State 0,2,3"""
    assert t800006000_x41()
    """State 1"""
    c1_120(1103)
    Quit()

def t800006000_2000():
    """State 0,2,3"""
    assert t800006000_x42(val1=10, z1=12)
    """State 1"""
    c1_120(2000)
    Quit()

def t800006000_x0(action1=_):
    """State 0,1"""
    OpenGenericDialog(8, action1, 3, 4, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == 1:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t800006000_x1(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t800006000_x2():
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

def t800006000_x3():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t800006000_x4(lot1=100420):
    """State 0,1"""
    # lot:100420:Glowstone
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t800006000_x5(val3=10, val4=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val3 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t800006000_x21()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val4 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t800006000_x2()
    else:
        """State 4,7"""
        call = t800006000_x34()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val4 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t800006000_x2()
    """State 9"""
    return 0

def t800006000_x6():
    """State 0,1"""
    assert t800006000_x2()
    """State 2"""
    return 0

def t800006000_x7(flag1=4703, flag2=4701, flag3=4702, val2=5, val3=10, val4=12, val5=10, val6=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z2=1, z3=1000000, z4=1000000,
                  z5=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t800006000_x24(flag1=flag1, flag2=flag2, flag3=flag3, val2=val2, val3=val3, val4=val4,
                              val5=val5, val6=val6, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z2=z2, z3=z3, z4=z4, z5=z5, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t800006000_x23()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t800006000_x8(val2=5, val3=10, val4=12, val5=10, val6=12, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z2=1, z3=1000000, z4=1000000, z5=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t800006000_x11(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z3=z3, z4=z4, z5=z5)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t800006000_x15(val2=val2, z2=z2)
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
        elif GetEventFlag(flag6) == 1 and not GetEventFlag(flag7) and GetDistanceToPlayer() < val5:
            """State 5"""
            call = t800006000_x17(val6=val6)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val6 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t800006000_x28() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t800006000_x13(val3=val3, val4=val4)
    """Unused"""
    """State 7"""
    return 0

def t800006000_x9(val3=10, val4=12):
    """State 0,1"""
    call = t800006000_x19(val3=val3, val4=val4)
    assert IsPlayerDead() == 1
    """State 2"""
    t800006000_x5(val3=val3, val4=val4)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t800006000_x10(flag1=4703, val3=10, val4=12):
    """State 0,8"""
    assert t800006000_x36()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val3:
            """State 4,6"""
            call = t800006000_x22()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val4 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t800006000_x2()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t800006000_x11(actionbutton1=6000, flag4=6000, flag5=6001, z3=1000000, z4=1000000, z5=1000000):
    """State 0,1"""
    call = t800006000_x12(z6=2000, val7=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t800006000_x1(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800006000_x12(z6=_, val7=_):
    """State 0,1"""
    if f203(z6) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z6)
        assert f202() == val7
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t800006000_x13(val3=10, val4=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t800006000_x2()
    """State 3"""
    if GetDistanceToPlayer() < val3:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t800006000_x14()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val4 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t800006000_x29()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t800006000_x14():
    """State 0,1"""
    assert t800006000_x12(z6=1101, val7=1101)
    """State 2"""
    return 0

def t800006000_x15(val2=5, z2=1):
    """State 0,2"""
    assert t800006000_x25()
    """State 1"""
    call = t800006000_x16()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val2 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t800006000_x27()
    """State 4"""
    return 0

def t800006000_x16():
    """State 0,1"""
    assert t800006000_x12(z6=1000, val7=1000)
    """State 2"""
    return 0

def t800006000_x17(val6=12):
    """State 0,1"""
    call = t800006000_x18()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val6 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t800006000_x28()
    """State 3"""
    return 0

def t800006000_x18():
    """State 0,1"""
    assert t800006000_x12(z6=1100, val7=1100)
    """State 2"""
    return 0

def t800006000_x19(val3=10, val4=12):
    """State 0,5"""
    assert t800006000_x36()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val3
        """State 3"""
        call = t800006000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val4 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t800006000_x30()
    """Unused"""
    """State 6"""
    return 0

def t800006000_x20():
    """State 0,2"""
    call = t800006000_x12(z6=1102, val7=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t800006000_x21():
    """State 0,1"""
    assert t800006000_x12(z6=1001, val7=1001)
    """State 2"""
    return 0

def t800006000_x22():
    """State 0,1"""
    assert t800006000_x12(z6=1103, val7=1103)
    """State 2"""
    return 0

def t800006000_x23():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t800006000_x24(flag1=4703, flag2=4701, flag3=4702, val2=5, val3=10, val4=12, val5=10, val6=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z2=1, z3=1000000, z4=1000000,
                   z5=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t800006000_x8(val2=val2, val3=val3, val4=val4, val5=val5, val6=val6, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z2=z2,
                             z3=z3, z4=z4, z5=z5, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t800006000_x10(flag1=flag1, val3=val3, val4=val4)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t800006000_x9(val3=val3, val4=val4)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t800006000_x35() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t800006000_x25():
    """State 0,1"""
    assert t800006000_x26()
    """State 2"""
    return 0

def t800006000_x26():
    """State 0,1"""
    assert t800006000_x12(z6=1104, val7=1104)
    """State 2"""
    return 0

def t800006000_x27():
    """State 0,1"""
    call = t800006000_x12(z6=1201, val7=1201)
    if call.Get() == 1:
        """State 2"""
        assert t800006000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800006000_x28():
    """State 0,1"""
    call = t800006000_x12(z6=1300, val7=1300)
    if call.Get() == 1:
        """State 2"""
        assert t800006000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800006000_x29():
    """State 0,1"""
    call = t800006000_x12(z6=1301, val7=1301)
    if call.Get() == 1:
        """State 2"""
        assert t800006000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800006000_x30():
    """State 0,1"""
    call = t800006000_x12(z6=1302, val7=1302)
    if call.Get() == 1:
        """State 2"""
        assert t800006000_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800006000_x31(text2=_, mode4=1):
    """State 0,4"""
    assert t800006000_x3() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text2, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode4:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t800006000_x32(text1=_, mode3=1):
    """State 0,4"""
    assert t800006000_x33() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text1, -1, -1, 1)
    """State 3"""
    if not mode3:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t800006000_x33():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t800006000_x34():
    """State 0,1"""
    assert t800006000_x12(z6=1002, val7=1002)
    """State 2"""
    return 0

def t800006000_x35():
    """State 0,1"""
    assert t800006000_x2()
    """State 2"""
    return 0

def t800006000_x36():
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

def t800006000_x37():
    """State 0,1"""
    if GetEventFlag(4705) == 1:
        """State 3"""
        assert t800006000_x43()
    else:
        """State 2"""
        pass
    """State 8"""
    Label('L0')
    return 0
    """Unused"""
    """State 4"""
    assert t800006000_x44()
    Goto('L0')
    """State 5"""
    assert t800006000_x45()
    Goto('L0')
    """State 6"""
    assert t800006000_x46()
    Goto('L0')
    """State 7"""
    assert t800006000_x47()
    Goto('L0')

def t800006000_x38():
    """State 0,2,6"""
    # talk:80080300:"Is that all you were, mate?"
    assert t800006000_x32(text1=80080300, mode3=1)
    """State 7"""
    Label('L0')
    return 0
    """Unused"""
    """State 1"""
    Goto('L1')
    """State 3,4"""
    Goto('L0')
    """State 5"""
    Label('L1')
    # talk:80081300:"I'll never forgive your kind..."
    assert t800006000_x32(text1=80081300, mode3=1)
    Goto('L0')

def t800006000_x39():
    """State 0,1,3,7"""
    assert t800006000_x78()
    """State 8"""
    Label('L0')
    return 0
    """Unused"""
    """State 2"""
    Goto('L1')
    """State 4,5"""
    Goto('L0')
    """State 6"""
    Label('L1')
    assert t800006000_x79()
    Goto('L0')

def t800006000_x40():
    """State 0,2"""
    if not GetEventFlag(1042369303):
        """State 3,7"""
        SetEventFlag(1042369303, 1)
        """State 6"""
        SetEventFlag(1042362710, 1)
        """State 9,11,15"""
        # talk:80080200:"I knew you for a highwayman all along."
        assert t800006000_x32(text1=80080200, mode3=1)
    elif not GetEventFlag(1042362710):
        """State 4,8"""
        SetEventFlag(1042362710, 1)
    else:
        """State 5"""
        pass
    """State 1"""
    Label('L0')
    Quit()
    """Unused"""
    """State 10"""
    Goto('L1')
    """State 12,13"""
    Goto('L0')
    """State 14"""
    Label('L1')
    # talk:80081200:"I see. I see how it is! You were one of them all along!"
    assert t800006000_x32(text1=80081200, mode3=1)
    Goto('L0')
    """State 16"""
    return 0

def t800006000_x41():
    """State 0,2,6"""
    # talk:80080400:"Is this...how it ends?"
    assert t800006000_x32(text1=80080400, mode3=1)
    """State 7"""
    Label('L0')
    return 0
    """Unused"""
    """State 1"""
    Goto('L1')
    """State 3,4"""
    Goto('L0')
    """State 5"""
    Label('L1')
    # talk:80081400:"Your kind...will all be razed clean."
    assert t800006000_x32(text1=80081400, mode3=1)
    Goto('L0')

def t800006000_x42(val1=10, z1=12):
    """State 0"""
    while True:
        """State 4"""
        Label('L0')
        if GetEventFlag(4705) == 1:
            """State 2,9"""
            call = t800006000_x77()
            if call.Done():
                break
            elif not GetEventFlag(4705):
                pass
        elif GetEventFlag(4717) == 1:
            """State 5,6"""
            assert not GetEventFlag(4717)
        else:
            """State 3,7"""
            # actionbutton:6000:"Talk"
            call = t800006000_x1(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000,
                                 flag12=6000, flag4=6000)
            if call.Done():
                break
            elif GetEventFlag(4705) == 1 or GetEventFlag(4709) == 1:
                pass
    """State 10"""
    Label('L1')
    return 0
    """Unused"""
    """State 1,8"""
    call = t800006000_x76(val1=val1, z1=z1)
    if call.Done():
        Goto('L1')
    elif not GetEventFlag(4709):
        Goto('L0')

def t800006000_x43():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(20008, -1)
    assert t800006000_x50()
    """State 2"""
    return 0

def t800006000_x44():
    """State 0,1"""
    assert t800006000_x58()
    """State 2"""
    return 0

def t800006000_x45():
    """State 0,1"""
    assert t800006000_x65()
    """State 2"""
    return 0

def t800006000_x46():
    """State 0,1"""
    if not GetEventFlag(35000500):
        """State 2"""
        assert t800006000_x74()
    else:
        """State 3"""
        assert t800006000_x75()
    """State 4"""
    return 0

def t800006000_x47():
    """State 0,3"""
    if not GetEventFlag(35000500):
        """State 4,6"""
        # talk:80007100:"The frenzied flame...burned me..."
        def WhilePaused():
            RequestAnimation(20041, -1)
        assert t800006000_x31(text2=80007100, mode4=1)
    else:
        """State 5,7"""
        # talk:80001500:"The howl of a wolf, in the Mistwood..."
        def WhilePaused():
            RequestAnimation(20041, -1)
        assert t800006000_x31(text2=80001500, mode4=1)
    """State 1"""
    SetEventFlag(35009270, 1)
    """State 2"""
    Quit()
    """Unused"""
    """State 8"""
    return 0

def t800006000_x48():
    """State 0,1"""
    SetEventFlag(1042362712, 1)
    """State 2"""
    return 0

def t800006000_x49():
    """State 0,1"""
    if not GetEventFlag(1042369308):
        """State 2,6"""
        # talk:80000100:"You're a Tarnished, I can see it."
        assert t800006000_x31(text2=80000100, mode4=1)
        """State 9"""
        assert t800006000_x48()
        """State 5"""
        SetEventFlag(1042369308, 1)
    elif GetEventFlag(1042362712) == 1:
        """State 3,7"""
        assert t800006000_x53()
    else:
        """State 4,8"""
        assert t800006000_x52()
    """State 10"""
    return 0

def t800006000_x50():
    """State 0,1"""
    assert t800006000_x49()
    """State 2"""
    assert t800006000_x51()
    """State 3"""
    return 0

def t800006000_x51():
    """State 0,19"""
    SetEventFlag(1042369306, 0)
    """State 20"""
    SetEventFlag(1042369307, 0)
    """State 1"""
    c1_110()
    ClearTalkActionState()
    while True:
        """State 2"""
        ClearTalkListData()
        """State 27"""
        assert t800006000_x56()
        """State 29"""
        assert t800006000_x80()
        """State 3"""
        
        # Access Grand Repository
        AddTalkListData(10, 99999300, -1)
        
        # Sell
        AddTalkListData(12, 99999034, -1)
        
        # action:28000002:"About Kalé"
        AddTalkListDataIf(GetEventFlag(1042369319) == 1, 3, 28000002, -1)
        # action:28000004:"Talk"
        AddTalkListDataIf(GetEventFlag(1042369321) == 1, 3, 28000004, -1)
        # action:28000005:"Talk"
        AddTalkListDataIf(GetEventFlag(1042369322) == 1, 3, 28000005, -1)
        # action:28000014:"About the howling in Mistwood"
        AddTalkListDataIf(GetEventFlag(1042369320) == 1, 4, 28000014, -1)
        # action:28000015:"About Blaidd"
        AddTalkListDataIf(GetEventFlag(1042369325) == 1, 4, 28000015, -1)
        # goods:8500:Crafting Kit, action:28000003:"Recommendation"
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 8500, 1, 1, 0) == 1, 5, 28000003, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            """State 6"""
            # goods:8500:Crafting Kit
            if ComparePlayerInventoryNumber(3, 8500, 4, 1, 0) == 1:
                """State 13"""
                pass
            else:
                """State 14,12"""
                SetEventFlag(1042369306, 1)
            """State 10"""
            OpenTranspositionShop(8000000, 8999999)
            c1_141(5)
            """State 24"""
            call = t800006000_x54()
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 18"""
            # goods:8500:Crafting Kit
            if ComparePlayerInventoryNumber(3, 8500, 4, 1, 0) == 1:
                """State 15,17"""
                SetEventFlag(1042369307, 1)
            else:
                """State 16"""
                pass
        elif GetTalkListEntryResult() == 2:
            """State 7,11"""
            OpenSellShop(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 8,25"""
            assert t800006000_x55()
        elif GetTalkListEntryResult() == 4:
            """State 23,30"""
            assert t800006000_x81()
        elif GetTalkListEntryResult() == 5:
            """State 21,28"""
            # talk:80000800:"You know, if you can spare the runes,"
            assert t800006000_x31(text2=80000800, mode4=1)
            """State 22"""
            SetEventFlag(1042369314, 1)
        # Access Grand Repository
        elif GetTalkListEntryResult() == 10:
            """State 32"""
            assert t800006000_x100()
        # Sell
        elif GetTalkListEntryResult() == 12:
            OpenSellShop(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        else:
            """State 9,26"""
            assert t800006000_x57()
            """State 31"""
            return 0

def t800006000_x52():
    """State 0,1"""
    if not GetEventFlag(1042369311) and not GetEventFlag(4707):
        """State 2,4"""
        # talk:80000300:"Wait, weren't you...?"
        assert t800006000_x31(text2=80000300, mode4=1)
    else:
        """State 3,5"""
        # talk:80000400:"Ah, it's you again."
        assert t800006000_x31(text2=80000400, mode4=1)
    """State 6"""
    assert t800006000_x48()
    """State 7"""
    return 0

def t800006000_x53():
    """State 0,1"""
    # talk:80000200:"What is it? Still going to purchase something?"
    assert t800006000_x31(text2=80000200, mode4=1)
    """State 2"""
    return 0

def t800006000_x54():
    """State 0"""
    assert DidYouDoSomethingInTheMenu(0) == 1
    """State 12"""
    if not GetEventFlag(1042362713):
        """State 1,11"""
        SetEventFlag(1042362713, 1)
        """State 3"""
        if not GetEventFlag(1042369309):
            """State 4,7"""
            SetEventFlag(1042369309, 1)
        elif not GetEventFlag(1042369310):
            """State 5,8"""
            SetEventFlag(1042369310, 1)
        else:
            """State 6,9"""
            SetEventFlag(1042369311, 1)
    else:
        """State 2"""
        pass
    """State 10"""
    Quit()
    """Unused"""
    """State 13"""
    return 0

def t800006000_x55():
    """State 0,1"""
    if GetEventFlag(1042369319) == 1:
        """State 2,9"""
        # talk:80000700:"I am of a nomadic people."
        assert t800006000_x31(text2=80000700, mode4=1)
        """State 5"""
        SetEventFlag(1042369313, 1)
        """State 6"""
        SetEventFlag(1042362714, 1)
    elif GetEventFlag(1042369321) == 1:
        """State 3,10"""
        # talk:80001000:"There are others of my people who yet survive in these lands."
        assert t800006000_x31(text2=80001000, mode4=1)
        """State 7"""
        SetEventFlag(1042369315, 1)
    else:
        """State 4,11"""
        # talk:80001200:"Perhaps you don't need to hear this, but..."
        assert t800006000_x31(text2=80001200, mode4=1)
        """State 8"""
        SetEventFlag(1042369317, 1)
    """State 12"""
    return 0

def t800006000_x56():
    """State 0,1"""
    SetEventFlag(1042369319, 0)
    SetEventFlag(1042369321, 0)
    SetEventFlag(1042369322, 0)
    """State 2"""
    if not GetEventFlag(1042369313):
        """State 3"""
        SetEventFlag(1042369319, 1)
    elif GetEventFlag(1042369313) == 1 and not GetEventFlag(1042362714) and not GetEventFlag(1042369315):
        """State 4"""
        SetEventFlag(1042369321, 1)
    elif GetEventFlag(1042369315) == 1 and not GetEventFlag(1042369317):
        """State 5"""
        SetEventFlag(1042369322, 1)
    else:
        """State 6"""
        pass
    """State 7"""
    return 0

def t800006000_x57():
    """State 0,1"""
    if GetEventFlag(1042369306) == 1 and GetEventFlag(1042369307) == 1 and GetEventFlag(1042369314) == 1:
        """State 2,4"""
        # talk:80000900:"I'm glad you took my warning to heart."
        assert t800006000_x31(text2=80000900, mode4=1)
    else:
        """State 3,5"""
        assert t800006000_x63()
    """State 6"""
    return 0

def t800006000_x58():
    """State 0,1"""
    assert t800006000_x59()
    """State 2"""
    assert t800006000_x60()
    """State 3"""
    return 0

def t800006000_x59():
    """State 0,1"""
    if not GetEventFlag(1037429255) and not GetEventFlag(1042369311):
        """State 2,7"""
        # talk:80003100:"We meet again, I see."
        assert t800006000_x31(text2=80003100, mode4=1)
        """State 11"""
        Label('L0')
        assert t800006000_x48()
        """State 6"""
        SetEventFlag(1037429255, 1)
    elif not GetEventFlag(1037429255) and GetEventFlag(1042369311) == 1:
        """State 3,8"""
        # talk:80003000:"Ah, good to see you."
        assert t800006000_x31(text2=80003000, mode4=1)
        Goto('L0')
    elif GetEventFlag(1042362712) == 1:
        """State 4,9"""
        assert t800006000_x53()
    else:
        """State 5,10"""
        assert t800006000_x52()
    """State 12"""
    return 0

def t800006000_x60():
    """State 0,13"""
    SetEventFlag(1037429258, 0)
    """State 1"""
    c1_110()
    ClearTalkActionState()
    while True:
        """State 2"""
        ClearTalkListData()
        """State 18"""
        assert t800006000_x64()
        """State 3"""
        # action:20000010:"Purchase"
        AddTalkListData(1, 20000010, -1)
        # action:20000011:"Sell"
        AddTalkListData(2, 20000011, -1)
        # action:28000013:""
        AddTalkListDataIf(GetEventFlag(1037429264) == 1, 3, 28000013, -1)
        # action:28000008:""
        AddTalkListDataIf(GetEventFlag(1037429265) == 1, 3, 28000008, -1)
        # action:28000009:""
        AddTalkListDataIf(GetEventFlag(1037429266) == 1, 3, 28000009, -1)
        # action:28000010:""
        AddTalkListDataIf(GetEventFlag(1037429267) == 1, 3, 28000010, -1)
        # goods:1200:Gold-Pickled Fowl Foot
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 1200, 4, 1, 0) == 1, 4, 28000000, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            """State 6,11"""
            OpenRegularShop(100625, 100649)
            """State 14"""
            call = t800006000_x54()
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 7,12"""
            OpenSellShop(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 8,15"""
            assert t800006000_x61()
        elif GetTalkListEntryResult() == 4:
            """State 9,16"""
            assert t800006000_x62()
        else:
            """State 10,17"""
            assert t800006000_x71()
            """State 19"""
            return 0

def t800006000_x61():
    """State 0,1"""
    if GetEventFlag(1037429264) == 1:
        """State 2,10"""
        # talk:80003200:"Have you seen a crow around here by any chance?"
        assert t800006000_x31(text2=80003200, mode4=1)
        """State 6"""
        SetEventFlag(1037429260, 1)
    elif GetEventFlag(1037429265) == 1:
        """State 3,11"""
        # talk:80003400:"So, about the letter you brought me..."
        assert t800006000_x31(text2=80003400, mode4=1)
        """State 7"""
        SetEventFlag(1037429261, 1)
    elif GetEventFlag(1037429266) == 1:
        """State 4,12"""
        # talk:80003600:"I've always preferred my own company, to that of other people's..."
        assert t800006000_x31(text2=80003600, mode4=1)
        """State 8"""
        SetEventFlag(1037429262, 1)
    else:
        """State 5,13"""
        # talk:80003500:"Once I decipher that cryptogram, I'll be packing up shop again."
        assert t800006000_x31(text2=80003500, mode4=1)
        """State 9"""
        SetEventFlag(1037429263, 1)
    """State 14"""
    return 0

def t800006000_x62():
    """State 0,8"""
    call = t800006000_x0(action1=28001001)
    if call.Get() == 0:
        """State 2,1"""
        # goods:1200:Gold-Pickled Fowl Foot
        PlayerEquipmentQuantityChange(3, 1200, -1)
        """State 4"""
        ChangePlayerStat(8, 0, 2000)
        """State 5"""
        SetEventFlag(1037429256, 1)
        """State 7"""
        SetEventFlag(1037422710, 1)
        """State 6"""
        SetEventFlag(1037429258, 1)
        """State 9"""
        # talk:80003300:"My thanks. I've been wanting to get my hands on this."
        assert t800006000_x31(text2=80003300, mode4=1)
    elif call.Done():
        """State 3"""
        pass
    """State 10"""
    return 0

def t800006000_x63():
    """State 0,1"""
    if DidYouDoSomethingInTheMenu(0) == 1:
        """State 2,4"""
        # talk:80000600:"Good-bye. Nice to do business."
        assert t800006000_x31(text2=80000600, mode4=1)
    else:
        """State 3,5"""
        # talk:80000500:"Good-bye for now."
        assert t800006000_x31(text2=80000500, mode4=1)
    """State 6"""
    return 0

def t800006000_x64():
    """State 0,2"""
    SetEventFlag(1037429264, 0)
    SetEventFlag(1037429265, 0)
    SetEventFlag(1037429266, 0)
    SetEventFlag(1037429267, 0)
    """State 1"""
    # goods:1200:Gold-Pickled Fowl Foot
    if ComparePlayerInventoryNumber(3, 1200, 1, 1, 0) == 1 and not GetEventFlag(1037429256):
        """State 3"""
        SetEventFlag(1037429264, 1)
    elif not GetEventFlag(1037422710) and GetEventFlag(1037429256) == 1 and not GetEventFlag(1037429261):
        """State 4"""
        SetEventFlag(1037429265, 1)
    elif GetEventFlag(1037429261) == 1 and not GetEventFlag(1037429262):
        """State 5"""
        SetEventFlag(1037429266, 1)
    elif GetEventFlag(1037429262) == 1 and GetEventFlag(62200) == 1:
        """State 6"""
        SetEventFlag(1037429267, 1)
    else:
        """State 7"""
        pass
    """State 8"""
    return 0

def t800006000_x65():
    """State 0,1"""
    assert t800006000_x66()
    """State 2"""
    assert t800006000_x67()
    """State 3"""
    return 0

def t800006000_x66():
    """State 0,1"""
    if not GetEventFlag(11009305):
        """State 2,6"""
        # talk:80005000:"Ah, good to see you."
        assert t800006000_x31(text2=80005000, mode4=1)
        """State 7"""
        assert t800006000_x48()
        """State 5"""
        SetEventFlag(11009305, 1)
    elif GetEventFlag(1042362712) == 1:
        """State 3,8"""
        assert t800006000_x53()
    else:
        """State 4,9"""
        assert t800006000_x52()
    """State 10"""
    return 0

def t800006000_x67():
    """State 0,13"""
    SetEventFlag(11009309, 0)
    """State 1"""
    c1_110()
    ClearTalkActionState()
    while True:
        """State 2"""
        ClearTalkListData()
        """State 18"""
        assert t800006000_x73()
        """State 3"""
        # action:20000010:"Purchase"
        AddTalkListData(1, 20000010, -1)
        # action:20000011:"Sell"
        AddTalkListData(2, 20000011, -1)
        # action:28000011:""
        AddTalkListDataIf(GetEventFlag(11009311) == 1, 3, 28000011, -1)
        # action:28000012:""
        AddTalkListDataIf(GetEventFlag(11009312) == 1, 3, 28000012, -1)
        # goods:1210:Exalted Flesh
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 1210, 4, 1, 0) == 1, 4, 28000001, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            """State 6,11"""
            OpenRegularShop(100650, 100674)
            """State 14"""
            call = t800006000_x54()
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 7,12"""
            OpenSellShop(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 8,16"""
            assert t800006000_x70()
        elif GetTalkListEntryResult() == 4:
            """State 9,15"""
            assert t800006000_x68()
        else:
            """State 10,17"""
            assert t800006000_x72()
            """State 19"""
            return 0

def t800006000_x68():
    """State 0,13"""
    call = t800006000_x0(action1=28001002)
    if call.Get() == 0:
        """State 2,1"""
        # goods:1210:Exalted Flesh
        PlayerEquipmentQuantityChange(3, 1210, -1)
        """State 4"""
        ChangePlayerStat(8, 0, 2000)
        """State 5"""
        SetEventFlag(11009306, 1)
        """State 6"""
        SetEventFlag(11009309, 1)
        """State 14"""
        # talk:80005200:"Where...did you find this letter?"
        assert t800006000_x31(text2=80005200, mode4=1)
        """State 7"""
        ClearTalkListData()
        """State 8"""
        AddTalkListData(1, 28001003, -1)
        """State 9"""
        OpenConversationChoicesMenu(0)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 10"""
        if GetTalkListEntryResult() == 1:
            """State 11,15"""
            assert t800006000_x69()
        else:
            """State 12"""
            pass
    elif call.Done():
        """State 3"""
        pass
    """State 16"""
    return 0

def t800006000_x69():
    """State 0,2"""
    # talk:80005300:"I can't imagine how it ended up there..."
    assert t800006000_x31(text2=80005300, mode4=1)
    """State 1"""
    SetEventFlag(11009307, 1)
    """State 3"""
    # lot:100420:Glowstone
    assert t800006000_x4(lot1=100420)
    """State 4"""
    # talk:80005310:"I hope you can join me at the Great Caravan, in fact."
    assert t800006000_x31(text2=80005310, mode4=1)
    """State 5"""
    return 0

def t800006000_x70():
    """State 0,1"""
    if GetEventFlag(11009311) == 1:
        """State 2,5"""
        # talk:80005100:"Oh yes, about the cryptogram from the letter..."
        assert t800006000_x31(text2=80005100, mode4=1)
        """State 4"""
        SetEventFlag(11009310, 1)
    else:
        """State 3,6"""
        assert t800006000_x69()
    """State 7"""
    return 0

def t800006000_x71():
    """State 0,1"""
    if GetEventFlag(1037429258) == 1:
        """State 2,4"""
        # talk:80000600:"Good-bye. Nice to do business."
        assert t800006000_x31(text2=80000600, mode4=1)
    else:
        """State 3,5"""
        assert t800006000_x63()
    """State 6"""
    return 0

def t800006000_x72():
    """State 0,1"""
    if GetEventFlag(11009309) == 1:
        """State 2,4"""
        # talk:80000600:"Good-bye. Nice to do business."
        assert t800006000_x31(text2=80000600, mode4=1)
    else:
        """State 3,5"""
        assert t800006000_x63()
    """State 6"""
    return 0

def t800006000_x73():
    """State 0,1"""
    SetEventFlag(11009311, 0)
    SetEventFlag(11009312, 0)
    """State 2"""
    if not GetEventFlag(11009310):
        """State 3"""
        SetEventFlag(11009311, 1)
    elif GetEventFlag(11009306) == 1 and not GetEventFlag(11009307):
        """State 4"""
        SetEventFlag(11009312, 1)
    else:
        """State 5"""
        pass
    """State 6"""
    return 0

def t800006000_x74():
    """State 0,1"""
    if not GetEventFlag(35009255):
        """State 2,10"""
        # talk:80005400:"Ah, you, is it..."
        assert t800006000_x31(text2=80005400, mode4=1)
        """State 6"""
        SetEventFlag(35009255, 1)
    elif not GetEventFlag(35009256):
        """State 3,11"""
        # talk:80005500:"I'm sorry, but we won't be trading any longer."
        assert t800006000_x31(text2=80005500, mode4=1)
        """State 7"""
        SetEventFlag(35009256, 1)
    elif not GetEventFlag(35009257):
        """State 4,12"""
        # talk:80005600:"I should apologise to you."
        assert t800006000_x31(text2=80005600, mode4=1)
        """State 8"""
        SetEventFlag(35009257, 1)
    else:
        """State 5,13"""
        # talk:80005700:"I'm sorry, but we won't be trading any longer."
        assert t800006000_x31(text2=80005700, mode4=1)
        """State 9"""
        SetEventFlag(35009255, 1)
    """State 14"""
    return 0

def t800006000_x75():
    """State 0,1"""
    if not GetEventFlag(35009254):
        """State 2,5"""
        # talk:80005800:"Wait, what's that?"
        assert t800006000_x31(text2=80005800, mode4=1)
        """State 4"""
        SetEventFlag(35009254, 1)
    else:
        """State 3,6"""
        # talk:80005900:"Oh, that's it... That's what I need..."
        assert t800006000_x31(text2=80005900, mode4=1)
    """State 7"""
    return 0

def t800006000_x76(val1=10, z1=12):
    """State 0"""
    while True:
        """State 3"""
        SetEventFlag(35002710, 0)
        if GetEventFlag(4703) == 1:
            break
        elif not GetEventFlag(35002710) and GetDistanceToPlayer() < val1:
            """State 1"""
            SetEventFlag(35002710, 1)
            """State 4"""
            # talk:80007000:"O Three Fingers, throw wide the door."
            assert t800006000_x32(text1=80007000, mode3=1) and GetCurrentStateElapsedTime() > 35
    """State 2"""
    Quit()
    """Unused"""
    """State 5"""
    return 0

def t800006000_x77():
    """State 0"""
    while True:
        """State 3"""
        # actionbutton:6000:"Talk"
        call = t800006000_x1(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                             flag4=6000)
        if call.Done():
            break
        elif GetEventFlag(1042362715) == 1 and not GetEventFlag(1042362716):
            """State 1,2"""
            SetEventFlag(1042362716, 1)
            """State 4"""
            # talk:80080100:"What's the matter with you?"
            assert t800006000_x32(text1=80080100, mode3=1)
    """State 5"""
    return 0

def t800006000_x78():
    """State 0,1"""
    if not GetEventFlag(1042362711) and not GetEventFlag(1042362716):
        """State 2,6"""
        SetEventFlag(1042362711, 1)
        """State 10"""
        # talk:80080000:"Urgh!"
        assert t800006000_x32(text1=80080000, mode3=1)
    elif GetEventFlag(1042362711) == 1 and not GetEventFlag(1042362716):
        """State 3,8"""
        SetEventFlag(1042362716, 1)
        """State 11"""
        # talk:80080100:"What's the matter with you?"
        assert t800006000_x32(text1=80080100, mode3=1)
    elif not GetEventFlag(1042362711) and GetEventFlag(1042362716) == 1:
        """State 4,9"""
        SetEventFlag(1042362711, 1)
        """State 12"""
        # talk:80080000:"Urgh!"
        assert t800006000_x32(text1=80080000, mode3=1)
    else:
        """State 5"""
        """State 7"""
        pass
    """State 13"""
    return 0

def t800006000_x79():
    """State 0,1"""
    if not GetEventFlag(1042362711):
        """State 2,5"""
        SetEventFlag(1042362711, 1)
        """State 7"""
        # talk:80081000:"<takes damage>"
        assert t800006000_x32(text1=80081000, mode3=1)
    elif not GetEventFlag(1042362716):
        """State 3,6"""
        SetEventFlag(1042362716, 1)
        """State 8"""
        # talk:80081100:"So you're just like the others?"
        assert t800006000_x32(text1=80081100, mode3=1)
    else:
        """State 4"""
        pass
    """State 9"""
    return 0

def t800006000_x80():
    """State 0,1"""
    SetEventFlag(1042369320, 0)
    SetEventFlag(1042369325, 0)
    """State 2"""
    if GetEventFlag(1045379206) == 1 and not GetEventFlag(1045379205) and not GetEventFlag(1042369328):
        """State 3"""
        SetEventFlag(1042369320, 1)
    elif GetEventFlag(1045379205) == 1 and GetEventFlag(1042369328) == 1 and not GetEventFlag(1042369329):
        """State 4"""
        SetEventFlag(1042369325, 1)
    else:
        """State 5"""
        pass
    """State 6"""
    return 0

def t800006000_x81():
    """State 0,1"""
    if GetEventFlag(1042369320) == 1:
        """State 2,10"""
        # talk:80001500:"The howl of a wolf, in the Mistwood..."
        assert t800006000_x31(text2=80001500, mode4=1)
        """State 4"""
        SetEventFlag(1042369328, 1)
        if not GetEventFlag(60830):
            """State 6,9"""
            SetEventFlag(60830, 1)
            """State 8"""
            # gesture:73:Finger Snap
            AcquireGesture(73)
            assert GetCurrentStateElapsedTime() > 1
        else:
            """State 7"""
            pass
    else:
        """State 3,11"""
        # talk:80001700:"Oh, then you met Blaidd, did you?"
        assert t800006000_x31(text2=80001700, mode4=1)
        """State 5"""
        SetEventFlag(1042369329, 1)
    """State 12"""
    return 0


# Access Grand Repository
def t800006000_x100():
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
            assert t800006000_x101()
        # Browse Cut Content
        elif GetTalkListEntryResult() == 11:
            """State 33"""
            assert t800006000_x200()
        # Quick Start Options
        elif GetTalkListEntryResult() == 2:
            assert t800006000_x400()
        else:
            """State 12"""
            return 0

# Browse Inventory
def t800006000_x101():
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
            assert t800006000_x102()
        # Gestures
        elif GetTalkListEntryResult() == 11:
            """State 11"""
            assert t800006000_x110()
        # Runes
        elif GetTalkListEntryResult() == 12:
            assert t800006000_x312(99999013)
        else:
            """State 12"""
            return 0

# Items
def t800006000_x102():
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
def t800006000_x110():
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
        assert t800006000_x310(action3=99999700)
        return 0
    else:
        """State 5"""
        return 0

# Browse Cut Content
def t800006000_x200():
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
            assert t800006000_x210()
        else:
            """State 7"""
            return 0

# Gestures - Cut Content
def t800006000_x210():
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
        assert t800006000_x310(action3=99999701)
        return 0
    else:
        """State 5"""
        return 0
        
# Dialog
def t800006000_x301(action1=_):
    """State 0,1"""
    OpenGenericDialog(8, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0
    
# Yes/No prompt
def t800006000_x300(action3=_, z5=_, z6=_):
    """State 0"""
    assert t800006000_x301(action1=action3)
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
def t800006000_x310(action3=_):
    """State 0"""
    assert t800006000_x301(action1=action3)
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
def t800006000_x311(action3=_):
    """State 0"""
    assert t800006000_x301(action1=action3)
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
def t800006000_x312(action3=_):
    """State 0"""
    assert t800006000_x301(action1=action3)
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
def t800006000_x400():
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
            assert t800006000_x401()
        # Start Location Options
        elif GetTalkListEntryResult() == 2:
            assert t800006000_x402()
        else:
            """State 12"""
            return 0
    
# Progression Unlocks
def t800006000_x401():
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
            assert t800006000_x300(action3=99999602, z5=1047610162, z6=1)
            return 0
        # Unlock Access to Roundtable Hold
        elif GetTalkListEntryResult() == 2:
            assert t800006000_x300(action3=99999601, z5=1047610161, z6=1)
            return 0
        # Unlock Access to Torrent
        elif GetTalkListEntryResult() == 3:
            assert t800006000_x300(action3=99999600, z5=1047610160, z6=1)
            return 0
        # Unlock Flasks
        elif GetTalkListEntryResult() == 10:
            assert t800006000_x300(action3=99999810, z5=1047610200, z6=1)
            return 0
        # Unlock Crafting Kit
        elif GetTalkListEntryResult() == 11:
            assert t800006000_x300(action3=99999811, z5=1047610201, z6=1)
            return 0
        # Unlock Flask of Wondrous Physick
        elif GetTalkListEntryResult() == 12:
            assert t800006000_x300(action3=99999812, z5=1047610202, z6=1)
            return 0
        # Unlock Whetstone Knife
        elif GetTalkListEntryResult() == 13:
            assert t800006000_x300(action3=99999813, z5=1047610203, z6=1)
            return 0
        # Unlock Spirit Calling Bell
        elif GetTalkListEntryResult() == 14:
            assert t800006000_x300(action3=99999814, z5=1047610204, z6=1)
            return 0
        # Unlock Tailoring Tools
        elif GetTalkListEntryResult() == 15:
            assert t800006000_x300(action3=99999815, z5=1047610205, z6=1)
            return 0
        # Unlock Golden Tailoring Tools
        elif GetTalkListEntryResult() == 16:
            assert t800006000_x300(action3=99999816, z5=1047610206, z6=1)
            return 0
        # Unlock Talisman Pouches
        elif GetTalkListEntryResult() == 20:
            assert t800006000_x300(action3=99999800, z5=1047610210, z6=1)
            return 0
        # Unlock Memory Stones
        elif GetTalkListEntryResult() == 21:
            assert t800006000_x300(action3=99999801, z5=1047610211, z6=1)
            return 0
        # Unlock Cracked Pots
        elif GetTalkListEntryResult() == 22:
            assert t800006000_x300(action3=99999802, z5=1047610212, z6=1)
            return 0
        # Unlock Ritual Pots
        elif GetTalkListEntryResult() == 23:
            assert t800006000_x300(action3=99999803, z5=1047610213, z6=1)
            return 0
        # Unlock Perfume Bottles
        elif GetTalkListEntryResult() == 24:
            assert t800006000_x300(action3=99999804, z5=1047610214, z6=1)
            return 0
        else:
            """State 12"""
            return 0
            
# Teleports
def t800006000_x402():
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
            assert t800006000_x300(action3=99999611, z5=1047610400, z6=1)
        # Teleport to Mohgwyn Palace
        elif GetTalkListEntryResult() == 2:
            assert t800006000_x300(action3=99999610, z5=1047610401, z6=1)
        # Teleport to Stormveil Castle
        elif GetTalkListEntryResult() == 3:
            assert t800006000_x300(action3=99999612, z5=1047610402, z6=1)
        # Teleport to Leyndell, Royal Capital
        elif GetTalkListEntryResult() == 4:
            assert t800006000_x300(action3=99999613, z5=1047610403, z6=1)
        # Teleport to Miquella's Haligtree
        elif GetTalkListEntryResult() == 5:
            assert t800006000_x300(action3=99999614, z5=1047610404, z6=1)
        # Teleport to Crumbling Farum Azula
        elif GetTalkListEntryResult() == 6:
            assert t800006000_x300(action3=99999615, z5=1047610405, z6=1)
        # Teleport to Academy of Raya Lucaria
        elif GetTalkListEntryResult() == 7:
            assert t800006000_x300(action3=99999616, z5=1047610406, z6=1)
        # Teleport to Volcano Manor
        elif GetTalkListEntryResult() == 8:
            assert t800006000_x300(action3=99999617, z5=1047610407, z6=1)
        # Teleport to Redmane Castle
        elif GetTalkListEntryResult() == 9:
            assert t800006000_x300(action3=99999618, z5=1047610408, z6=1)
        # Teleport to Consecrated Snowfield
        elif GetTalkListEntryResult() == 10:
            assert t800006000_x300(action3=99999619, z5=1047610409, z6=1)
        # Teleport to Mountaintops of the Giants
        elif GetTalkListEntryResult() == 11:
            assert t800006000_x300(action3=99999620, z5=1047610410, z6=1)
        else:
            """State 12"""
            return 0
            