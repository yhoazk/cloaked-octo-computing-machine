#!/usr/bin/wish
proc write_n {} {
    .ent insert end "$::number"
    #open "out.out" w+
    set out [open "out.out" w+]
    puts $out "$::number"
}
entry .ent
button .but -text "asdas" -command "write_n"
set number 1
spinbox .spn -from 1 -to 20 -increment 2 -textvariable number -command "write_n"
pack .but
pack .spn
pack .ent

