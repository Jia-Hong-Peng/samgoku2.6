#_/_/_/_/_/_/_/_/_/#
#_/�@�@�|ĳ�ǡ@�@_/#
#_/_/_/_/_/_/_/_/_/#

sub COUNTRY_TALK {

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN("$kcon");
    if($xcid eq 0){&ERR("�L���ݰꤣ��ϥΡC");}
	$sno = $kclass / 500;
	if($sno > 20){$sno = 20;}

	open(IN,"$BBS_LIST") or &ERR('�S�}���Cerr no :country_bbs');
	@BBS_DATA = <IN>;
	close(IN);


	&HEADER;

	print <<"EOM";
<div align="center">
<TABLE WIDTH="70%" height=100%>
<TBODY><TR>
<TD BGCOLOR=$ELE_BG[$xele] WIDTH=100% height=5><div align="center"><font color=$ELE_C[$xele] size=4>�ա�<B> * $xname �|ĳ�� *</B>�֡�</font></div></TD>
</TR><TR>
<TD height=5>
<TABLE border="0"><TBODY>
<TR>
<TD></TD>
<TD WIDTH=100% align=center>
<TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>

<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>�Z�O</TD><TH>$kstr</TH><TD>���O</TD><TH>$kint</TH><TD>�βv�O</TD><TH>$klea</TH></TR>
<TR><TD>��</TD><TH>$kgold</TH><TD>��</TD><TH>$krice</TH><TD>�^�m</TD><TH>$kcex</TH></TR>
<TR><TD>���ݰ�</TD><TH colspan=2>$cou_name[$kcon]��</TH><TD>�L�h</TD><TH>$ksol</TH><TD>�V�m</TD><TH>$kgat</TH></TR>
</TBODY></TABLE>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="��^����"></form>
</TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD height="5">
<TABLE border="0" width=100%><TBODY>
<TR><TD width="100%" bgcolor=$TALK_BG><div align="center"><font color=$TALK_FONT>����M�Ϊ����i�O�C<BR>�۰�x����y�ϥΡC</font></div></TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD align=center>

<br><form action="./mydata.cgi" method="post">
<font color="#FFFFFF">�D�D�G</font><input type=text name=title size=40><p>
<font color="#FFFFFF">���e�G</font><textarea name=ins cols=40 rows=7>
</TEXTAREA> <img src="$IMG/$kchara.gif"><p>

<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=COUNTRY_WRITE>
<input type=submit value="�e�X">
</form>
</font>
EOM
	$BBS_NEXT_NUM = 20;

	if($in{'bbs_no'} eq ""){
		$bbs_no = 0;
	}else{
		$bbs_no = $in{'bbs_no'};
	}

	$s_n = 0;
	$n = 0;
	foreach(@BBS_DATA){
		($bbid,$bbtitle,$bbmes,$bbcharaimg,$bbname,$bbhost,$bbtime,$bbele,$bbcon,$bbtype,$bbno,$bbheap)=split(/<>/);
		if($kcon eq "$bbcon" && $bbtype eq "0"){
			if(!$bbheap){
				if($s_n >= $bbs_no && $s_n < $bbs_no + $BBS_NEXT_NUM){
				$bno = $s_n+1;
				$bb_id[$n] = $bbno;
				$n++;
				$c_mes[$bbno] = "<TABLE border=0 width=70% bgcolor=$ELE_C[$bbele]>

  <TBODY>
    <TR>
      <TD colspan=2 bgcolor=$ELE_BG[$xele]><B><font size=3 color=$ELE_C[$bbele]>$bno ��$bbtitle</font></B></TD>
    </TR>
    <TR>
      <TD width=80 rowspan=3 valign=middle align=center><img src=$IMG/$bbcharaimg.gif></TD>
      <TD>
      <TABLE border=0 width=100% bgcolor=$ELE_C[$bbele]>
        <TBODY>
          <TR>
            <TD width=100% bgcolor=$ELE_BG[$bbele]><font color=ffffff>$bbmes</TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
    <TR>
      <TD><font size=1 color=$ELE_BG[$bbele]>$bbname </font></TD>
    </TR>
    <TR>
      <TD colspan=2 align=right><font size=1 color=$ELE_BG[$bbele]>$bbtime</font></TD>
    </TR>

    <TR>
      <TD colspan=2 align=right>
<form action=\"./mydata.cgi\" method=\"post\">
<input type=text name=ins size=65>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=b_no value=$bbno>
<input type=hidden name=mode value=COUNTRY_WRITE>
<input type=submit value=�T�w>
</TD></TR></form>";
				}
			$s_n++;
			}
		}
	}

	foreach(@BBS_DATA){
		($bbid,$bbtitle,$bbmes,$bbcharaimg,$bbname,$bbhost,$bbtime,$bbele,$bbcon,$bbtype,$bbno,$bbheap)=split(/<>/);
		if($kcon eq "$bbcon" && $bbtype eq "0"){
			if($bbheap){
				$l=0;
				foreach(@bb_id){
					if($bbheap eq $bb_id[$l]){
					$c_mes[$bbheap] .= "<TR><TD colspan=2 width=100%><TABLE cellspacing=1 width=100% bgcolor=$ELE_BG[$bbele]><TBODY bgcolor=$ELE_C[$bbele]><TR><TD width=100%><font color=$ELE_BG[$bbele]>$bbmes</TD><TD bgcolor=$ELE_BG[$bbele]><img src=$IMG/$bbcharaimg.gif></TD></TR><TR><TD colspan=2><font size=1 color=$ELE_BG[$bbele]>$bbname <small>\[$bbtime\]</small></TD></TR></TABLE></TD></TR>";
					}
					$l++;
				}
			}
		}
	}

	$s=@c_mes;
	$d=0;
	foreach(@c_mes){
		$new_c_mes[$s] = $c_mes[$d];
		$s--;
		$d++;
	}

	foreach(@new_c_mes){
		if($_ ne ""){
			print "$_ </TBODY></TABLE><p>";
		}
	}

	$q=0;
	$n_bbs = $bbs_no + $BBS_NEXT_NUM;
	if($s_n >= $n_bbs){
	print " <form action=\"./mydata.cgi\" method=\"post\">
<input type=hidden name=mode value=COUNTRY_TALK>
<input type=hidden name=bbs_no value=$n_bbs>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=submit value=\"��$BBS_NEXT_NUM��\">
</form>";
	}
print <<"EOM";
</CENTER>
</TD>
</TR>
</TBODY></TABLE></div><center>
EOM

	&FOOTER;
	exit;
}
1;