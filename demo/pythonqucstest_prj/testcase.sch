<Qucs Schematic 0.0.15>
<Properties>
  <View=76,-59,1020,668,1.15528,0,0>
  <Grid=10,10,1>
  <DataSet=testcase.dat>
  <DataDisplay=testcase.dpl>
  <OpenDisplay=1>
  <showFrame=0>
  <FrameText0=Title>
  <FrameText1=Drawn By:>
  <FrameText2=Date:>
  <FrameText3=Revision:>
</Properties>
<Symbol>
</Symbol>
<Components>
  <GND * 1 130 140 0 0 0 0>
  <GND * 1 310 60 0 0 0 0>
  <Eqn Tsky 1 220 130 -31 16 0 0 "Tsky_K=10" 1 "Tsky_C=Tsky_K-273.15" 0 "yes" 0>
  <Pac SkyLoad 1 130 110 18 -26 0 1 "1" 0 "50 Ohm" 0 "0 W" 0 "1 GHz" 0 "Tsky_C" 0>
  <.AC SpectralResponse 1 120 210 0 46 0 0 "lin" 0 "35 GHz" 1 "50 GHz" 1 "151" 0 "yes" 0>
  <Pac OutputPort 1 700 150 18 -26 0 1 "2" 0 "50 Ohm" 0 "0 W" 0 "1 GHz" 0 "-273.15" 0>
  <GND * 1 700 190 0 0 0 0>
  <Amp BackendAmplifier 1 590 120 -26 27 0 0 "20" 1 "50 Ohm" 0 "50 Ohm" 0 "5 dB" 0>
  <.SP SP1 1 350 180 0 58 0 0 "lin" 1 "35 GHz" 1 "50 GHz" 1 "151" 1 "no" 0 "1" 0 "2" 0 "no" 0 "no" 0>
  <SPfile LNA 1 310 20 -26 -59 0 0 "lownoiseamplifier1.s2p" 1 "rectangular" 0 "linear" 0 "open" 0 "2" 0>
  <COAX Line1 1 430 50 -26 16 0 0 "2.29" 1 "0.022e-6" 0 "1" 0 "2.95 mm" 0 "0.9 mm" 0 "1500 mm" 1 "4e-4" 0 "26.85" 0>
  <Eqn OutputVolts 1 570 220 -31 16 0 0 "Freq_GHz=acfrequency*1e-9" 0 "s21db=dB(S[2,1])" 0 "outvolts_log=10*log10(out.vn)" 1 "outvolts_tot_V=sum(out.vn)" 1 "yes" 0>
</Components>
<Wires>
  <700 180 700 190 "" 0 0 0 "">
  <130 -20 130 80 "" 0 0 0 "">
  <620 120 700 120 "out" 674 70 70 "">
  <530 120 560 120 "" 0 0 0 "">
  <310 50 310 60 "" 0 0 0 "">
  <130 -20 280 -20 "fem_in" 180 10 120 "">
  <280 -20 280 20 "" 0 0 0 "">
  <340 20 360 20 "" 0 0 0 "">
  <530 50 530 120 "" 0 0 0 "">
  <460 50 530 50 "" 0 0 0 "">
  <360 20 360 50 "" 0 0 0 "">
  <360 50 400 50 "" 0 0 0 "">
  <460 50 460 50 "bem_in" 480 10 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
  <Text 530 -50 12 #000000 0 "python-qucs test circuit\nbuilt by Andrea Zonca\n\n">
</Paintings>
