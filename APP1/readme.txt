This is (will be) a fully featured combination of all dash subfeatures for a functional APP1
While file paths may need to be changed, (and os calls might need tweaking as well for docker), this is intended to fulfill the target capabilities of APP1 as shown in the project layout diagram

features:
generate unique directory ID
upload and save to directory
msconvert if raw; no convert required if fasta; no upload allowed if other
prints ID and path (todo output in a manner that can pass to APP2)

note: might move msconvert to APP3 in future to reduce user wait times within APP1
note2: APP3 intended to be run on a thread that is independent of user sessions, allowing the user to close the window and return to completed results later