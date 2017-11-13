#!/usr/bin/tclsh
require(tcltk)
tt <- tktoplevel()
SliderValue <- tclVar("50")
SliderValueLabel <- tklabel(tt,text=as.character(tclvalue(SliderValue)))
tkgrid(tklabel(tt,text="Slider Value : "),SliderValueLabel,tklabel(tt,text="%"))
tkconfigure(SliderValueLabel,textvariable=SliderValue)
slider <- tkscale(tt, from=100, to=0,
                   showvalue=F, variable=SliderValue,
                   resolution=1, orient="vertical")
tkgrid(slider)
tkfocus(tt)

