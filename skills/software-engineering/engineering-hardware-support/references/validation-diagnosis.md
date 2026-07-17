# Boot Fault Diagnosis

Symptom: PC powers on, fans spin, no display, no keyboard light.
Layer isolation: power present → POST not completing → before OS.
Tests: reseat RAM, boot one DIMM at a time, clear CMOS, test known-good PSU/GPU cable, check motherboard diagnostic LEDs.
Likely root cause: RAM seating/failure if one DIMM boots and pair fails.
Data safety: do not reinstall OS; storage is not implicated before POST.
