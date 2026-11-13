# STE-100 dictionary — grep-target lookup table

Derived from the **ASD-STE100 Issue 9** dictionary (Part 2), pages 2-1-A1 to
2-1-Y2. The PDF `ASD-STE100_ISSUE9.pdf` in this folder is the standard of
record; this file is a lookup aid generated from it. ASD-STE100 is a licensed
standard — this repository is private; do not redistribute this file or the PDF.

## How agents use this file

- **Never read this whole file.** Grep for one word at a time, e.g.
  `grep -i "^| accuracy " .agents/skills/language-persona/references/ste-100-dictionary.md`
  or `grep "^| AID (n) " ...`. Try both cases if unsure.
- **UPPERCASE word = APPROVED** in STE. Use it only as the listed part of
  speech; the middle column is its approved meaning (numbered when the word
  has several approved meanings).
- **lowercase word = NOT APPROVED.** The right column gives the approved
  alternative(s) to use instead, plus a "non-STE → STE" example pair when the
  entry has a single replacement.
- `(TN)` = technical noun, `(TV)` = technical verb: not listed as entries,
  but they appear as alternatives. A project's CONTEXT.md technical nouns and
  verbs are always permitted additions per STE rules 1.5 and 1.6.
- Restricted verb/adjective forms (conjugations, comparatives) are in the
  right column as `forms: ...` — use only those forms.
- Entries the parser could not classify confidently are under
  `## Needs manual review` at the bottom — verify them against the PDF.

| Word (pos) | Status / approved meaning | Use instead / notes |
|---|---|---|
| A (art) | Function word: indefinite article |  |
| abaft (prep) | NOT APPROVED | use: AFT OF (prep) — "The control unit is installed abaft the flight compartment." → "THE CONTROL UNIT IS INSTALLED AFT OF THE FLIGHT COMPARTMENT." |
| abandon (v) | NOT APPROVED | use: GO (v); STOP (v) |
| abate (v) | NOT APPROVED | use: DECREASE (v) — "When the wind speed abates to less than 30 knots, you can open the cargo door." → "WHEN THE WIND SPEED DECREASES TO LESS THAN 30 KNOTS, YOU CAN OPEN THE CARGO DOOR." |
| ability (n) | NOT APPROVED | use: CAN (v) — "One generator has the ability to supply power for all the systems." → "ONE GENERATOR CAN SUPPLY POWER FOR ALL THE SYSTEMS." |
| able (adj) | NOT APPROVED | use: CAN (v) — "If you are able to start the engine, do the applicable tests." → "IF YOU CAN START THE ENGINE, DO THE APPLICABLE TESTS." |
| abnormal (adj) | NOT APPROVED | use: UNUSUAL (adj); INCORRECT (adj) |
| abnormality (n) | NOT APPROVED | use: DEFECT (TN) — "Examine the seal for abnormalities." → "EXAMINE THE SEAL FOR DEFECTS." |
| ABOUT (prep) | Concerned with | For other meanings, use: APPROXIMATELY (adv); AROUND (prep) |
| ABOVE (prep) | In (or to) a position farther up than something | For other meanings, use: MORE THAN |
| ABRASIVE (adj) | That can remove material by friction |  |
| abrupt (adj) | NOT APPROVED | use: SUDDEN (adj); SUDDENLY (adv) |
| absence (n) | NOT APPROVED | use: NONE (pron); NOT (adv); NO (adj) |
| absent (adj) | NOT APPROVED | use: MISSING (adj); NO (adj) |
| absolutely (adv) | NOT APPROVED | use: FULLY (adv) — "Ensure the latch is absolutely engaged." → "MAKE SURE THAT THE LATCH IS FULLY ENGAGED." |
| ABSORB (v) | 1. To take up or into 2. To decrease the effect of | forms: ABSORBS, ABSORBED, ABSORBED |
| absorption (n) | NOT APPROVED | use: ABSORB (v) — "Measure the rate of absorption of the moisture by the silica gel." → "MEASURE THE TIME THAT IS NECESSARY FOR THE SILICA GEL TO ABSORB THE MOISTURE." |
| abundant (adj) | NOT APPROVED | use: LARGE (adj) — "Clean your skin with abundant clean water." → "CLEAN YOUR SKIN WITH A LARGE QUANTITY OF CLEAN WATER." |
| abut (v) | NOT APPROVED | use: TOUCH (v) — "The bin abuts the forward hinge surface." → "THE BIN TOUCHES THE FORWARD HINGE SURFACE." |
| accelerate (v) | NOT APPROVED | use: INCREASE (v); FASTER (adj) |
| ACCEPT (v) | To make a decision that something is satisfactory | forms: ACCEPTS, ACCEPTED, ACCEPTED |
| acceptable (adj) | NOT APPROVED | use: PERMITTED (adj); SATISFACTORY (adj); SERVICEABLE (adj) |
| acceptance (n) | NOT APPROVED | use: ACCEPT (v) — "Before acceptance of the unit, do the specified test procedure." → "BEFORE YOU ACCEPT THE UNIT, DO THE SPECIFIED TEST PROCEDURE." |
| ACCESS (n) | The ability to go into or near |  |
| accessible (adj) | NOT APPROVED | use: ACCESS (n) — "Rotate the cover until the jacks marked by + and -are accessible." → "TURN THE COVER UNTIL YOU CAN GET ACCESS TO THE JACKS THAT HAVE + AND - MARKS." |
| ACCIDENT (n) | An occurrence that causes injury or damage |  |
| ACCIDENTAL (adj) | That does not occur on purpose |  |
| ACCIDENTALLY (adv) | That does not occur on purpose |  |
| accommodate (v) | NOT APPROVED | use: LET (v) — "Studs are available in different lengths to accommodate different thicknesses of skin." → "DIFFERENT LENGTHS OF STUDS LET YOU ATTACH DIFFERENT THICKNESSES OF SKIN." |
| accomplish (v) | NOT APPROVED | use: DO (v); COMPLETE (v) — You can use a more accurate verb. |
| according to (prep) | NOT APPROVED | use: REFER (v) — "Calibrate the test set according to the manufacturer's instructions." → "TO CALIBRATE THE TEST SET, REFER TO THE MANUFACTURER'S INSTRUCTIONS." |
| account for (v) | NOT APPROVED | use: MAKE SURE (v) — "All tools and equipment must be accounted for." → "MAKE SURE THAT YOU REMOVE ALL TOOLS AND EQUIPMENT." |
| accumulate (v) | NOT APPROVED | use: COLLECT (v) — "If water accumulates in the filler line, drain it." → "IF WATER COLLECTS IN THE FILLER LINE, DRAIN IT." |
| accumulation (n) | NOT APPROVED | use: QUANTITY (n); COLLECT (v) |
| accuracy (n) | NOT APPROVED | use: PRECISION (n) — "The accuracy of the adjustment can vary." → "THE PRECISION OF THE ADJUSTMENT CAN CHANGE." |
| ACCURATE (adj) | Exact |  |
| ACCURATELY (adv) | Exactly |  |
| achieve (v) | NOT APPROVED | use: GET (v) — "Set the control to achieve maximum thrust." → "SET THE CONTROL TO GET MAXIMUM THRUST." |
| acquire (v) | NOT APPROVED | use: GET (v) — "The computer acquires this data from five sensors." → "THE COMPUTER GETS THIS DATA FROM FIVE SENSORS." |
| acrid (adj) | NOT APPROVED | use: DANGEROUS (adj) — "On contact with hot surfaces, this material produces acrid fumes." → "THIS MATERIAL RELEASES DANGEROUS FUMES WHEN IT TOUCHES HOT SURFACES." |
| ACROSS (prep) | From one side to the other side |  |
| act (v) | NOT APPROVED | Use an accurate verb. — "The hydraulic fluid flow acts on the valve." → "THE HYDRAULIC FLUID FLOW OPENS THE VALVE." |
| action (n) | NOT APPROVED | use: STEP (n); PROCEDURE (n); TASK (n) |
| ACTIVATE (v) | To make a system, function, or feature ready for operation | For other meanings, use: START (v) |
| ACTIVE (adj) | A system, function, or feature in a state of action |  |
| activity (n) | NOT APPROVED | use: TASK (n); PROCEDURE (n); WORK (n) |
| actuate (v) | NOT APPROVED | use: START (v); OPERATE (v); PUSH (v) |
| actuation (n) | NOT APPROVED | use: OPERATION (n) — "Monitor the actuation of the steering motor." → "MONITOR THE OPERATION OF THE STEERING MOTOR." |
| ADAPT (v) | To change or adjust to that which is necessary | forms: ADAPTS, ADAPTED, ADAPTED |
| ADD (v) | To increase the number, dimension, or quantity | forms: ADDS, ADDED, ADDED |
| addition (n) | NOT APPROVED | use: ADD (v) — "Adjust the clearance by the addition of special shims, as necessary." → "TO GET THE CORRECT CLEARANCE, ADD SPECIAL SHIMS, AS NECESSARY." |
| additional (adj) | NOT APPROVED | use: MORE (adj) — "This chapter gives additional information about safety." → "THIS CHAPTER GIVES MORE INFORMATION ABOUT SAFETY." |
| adequate (adj) | NOT APPROVED | use: SUFFICIENT (adj) — "Make sure that containers have adequate capacity and diameter." → "MAKE SURE THAT CONTAINERS HAVE SUFFICIENT CAPACITY AND DIAMETER." |
| adhere (v) | NOT APPROVED | use: BOND (v); OBEY (v) |
| adhesion (n) | NOT APPROVED | use: BOND (n) — "Clean the surface to ensure there will be good adhesion." → "CLEAN THE SURFACE TO MAKE SURE THAT THE BOND IS SATISFACTORY." |
| ADJACENT (adj) | That which is near to an object, with no other object of the same type between the two |  |
| ADJACENT TO (prep) | To be near to an object, with no other object of the same type between the two |  |
| adjoining (adj) | NOT APPROVED | use: ADJACENT (adj) — "Align the brackets with the adjoining components." → "ALIGN THE BRACKETS WITH THE ADJACENT COMPONENTS." |
| ADJUST (v) | To put in or come to a specified position or value | forms: ADJUSTS, ADJUSTED, ADJUSTED |
| ADJUSTABLE (adj) | That you can adjust |  |
| ADJUSTMENT (n) | The effect of adjusting |  |
| admit (v) | NOT APPROVED | use: LET (v) — "Open the valve to admit nitrogen into the oleo strut." → "OPEN THE VALVE TO LET NITROGEN GO INTO THE OLEO STRUT." |
| adopt (v) | NOT APPROVED | use: USE (v) — "Adopt this procedure if the unit is damaged." → "IF THE UNIT IS DAMAGED, USE THIS PROCEDURE." |
| advance (n) | NOT APPROVED | use: FORWARD (adj) — "The advance of the control lever must be slow and continuous." → "THE FORWARD MOVEMENT OF THE CONTROL LEVER MUST BE SLOW AND CONTINUOUS." |
| advance (v) | NOT APPROVED | use: SET (v); FORWARD (adv) |
| adverse (adj) | NOT APPROVED | use: BAD (adj) — If it is possible, give accurate and correct conditions. — "For parking in adverse weather conditions, refer to Chapter 6. This medication can cause adverse reactions." → "REFER TO CHAPTER 6 FOR INSTRUCTIONS ABOUT HOW TO PARK IN BAD WEATHER CONDITIONS. THIS MEDICATION CAN CAUSE DERMATITIS." |
| advisable (adj) | NOT APPROVED | use: RECOMMEND (v) — "According to the Design Authority, it is advisable to retorque the bolts at intervals of six months." → "THE DESIGN AUTHORITY RECOMMENDS THAT YOU TORQUE THE BOLTS AGAIN AT INTERVALS OF SIX MONTHS." |
| advise (v) | NOT APPROVED | use: TELL (v); RECOMMEND (v) |
| affect (v) | NOT APPROVED | use: EFFECT (n) — If it is possible, be accurate. — "Magnetic tools affect the compass system. This medication can affect your skin." → "MAGNETIC TOOLS HAVE AN UNWANTED EFFECT ON THE COMPASS SYSTEM. THIS MEDICATION CAN CAUSE DERMATITIS" |
| AFT (adj) | At or nearer to the rear of an air or sea vehicle |  |
| AFT (adv) | In the direction of the rear of an air or sea vehicle |  |
| AFTER (conj) | That follows a specified time, sequence, or operation |  |
| AFTER (prep) | That follows a specified time, sequence, or operation |  |
| AFT OF (prep) | At a position nearer to the rear |  |
| AGAIN (adv) | One more occurrence |  |
| AGAINST (prep) | In contact with |  |
| AGENT (n) | One of a group of materials made to do a specified task |  |
| aggravate (v) | NOT APPROVED | use: INCREASE (v) — "Tire wear is aggravated by high speed." → "TIRE WEAR INCREASES WITH HIGH SPEED." |
| agitate (v) | NOT APPROVED | use: SHAKE (v) — "Agitate the solution." → "SHAKE THE SOLUTION." |
| agitation (n) | NOT APPROVED | use: SHAKE (v) — "After agitation, do not use the solution for one hour." → "IF YOU SHAKE THE SOLUTION, DO NOT USE IT FOR ONE HOUR." |
| AGREE (v) | To be consistent with | forms: AGREES, AGREED, AGREED |
| ahead (adv) | NOT APPROVED | use: FORWARD (adv) — "When you install the antenna, the alignment arrow must point ahead." → "WHEN YOU INSTALL THE ANTENNA, THE ALIGNMENT ARROW MUST POINT FORWARD." |
| AID (n) | Help that is given |  |
| aid (v) | NOT APPROVED | use: HELP (v) — "Apply sand to the planks to aid tire traction." → "APPLY SAND TO THE PLANKS TO HELP WITH TIRE TRACTION." |
| aim (v) | NOT APPROVED | use: POINT (v) — "Do not aim the hose at persons." → "DO NOT POINT THE HOSE AT PERSONS." |
| AIRBORNE (adj) | In, or used in, flight |  |
| air-dry (v) | NOT APPROVED | use: DRY (v) — "Air-dry the filter." → "DRY THE FILTER IN THE AIR." |
| AIRFLOW (n) | A flow of air |  |
| alert (v) | NOT APPROVED | use: TELL (v) — "Alert all persons to go away from the area." → "TELL ALL PERSONS TO GO AWAY FROM THE AREA." |
| ALIGN (v) | To put or come into a specified position in relation to a line | forms: ALIGNS, ALIGNED, ALIGNED |
| alignment (n) | NOT APPROVED | use: ALIGN (v) — "Ensure that the keyway is at the top and in alignment with the peg." → "MAKE SURE THAT THE KEYWAY IS AT THE TOP AND ALIGNS WITH THE PEG." |
| ALL (adj) | Full quantity |  |
| allocate (v) | NOT APPROVED | use: GIVE (v) — "Allocate the different maintenance tasks to the approved technicians." → "GIVE THE DIFFERENT MAINTENANCE TASKS TO THE APPROVED TECHNICIANS." |
| allow (v) | NOT APPROVED | use: LET (v) — "Do not allow the cable to touch the floor." → "DO NOT LET THE CABLE TOUCH THE FLOOR." |
| allowable (adj) | NOT APPROVED | use: PERMITTED (adj); APPROVED (adj) |
| ALMOST (adv) | Near the limit or the value |  |
| ALONG (prep) | In a line parallel with the length or direction of |  |
| already (adv) | NOT APPROVED | use: IN PROGRESS (adv); NO OTHER — Frequently, an alternative for this word is not necessary. |
| ALSO (adv) | In addition |  |
| alter (v) | NOT APPROVED | use: CHANGE (v) — "It is possible that the installation of the connector pins altered the routing of the cable loom." → "IT IS POSSIBLE THAT THE INSTALLATION OF THE CONNECTOR PINS CHANGED THE ROUTING OF THE CABLE LOOM." |
| alteration (n) | NOT APPROVED | use: CHANGE (v) — "The alteration to this repair procedure must get approval of the Design Authority." → "IF YOU CHANGE THIS REPAIR PROCEDURE, GET APPROVAL OF THE DESIGN AUTHORITY." |
| alternate (adj) | NOT APPROVED | use: ALTERNATIVE (adj); EACH SECOND |
| alternate (v) | NOT APPROVED | use: THEN (adv) — "Alternate between pilot’s and copilot’s instrument test." → "DO THE PILOT’S INSTRUMENT TEST AND THEN THE COPILOT’S TEST." |
| alternately (adv) | NOT APPROVED | use: THEN THE OTHER — IN ONE (TN) … AND — "To make pin removal easier, manually turn the canopy alternately in the two directions." → "TO MAKE PIN REMOVAL EASIER, MANUALLY TURN THE CANOPY IN ONE DIRECTION AND THEN IN THE OTHER." |
| ALTERNATIVE (adj) | That gives a choice |  |
| ALTERNATIVE (n) | One of two or more objects or processes that have the same or almost the same properties or functions |  |
| alternatively (adv) | NOT APPROVED | use: ALTERNATIVE (n) — "Alternatively, you can do test B." → "YOU CAN DO TEST B AS AN ALTERNATIVE." |
| ALTHOUGH (conj) | In spite of the fact that |  |
| ALWAYS (adv) | At all times |  |
| amend (v) | NOT APPROVED | use: CHANGE (v) — "If it is necessary to amend the Repair Scheme, get the approval of the Design Authority." → "IF IT IS NECESSARY TO CHANGE THE REPAIR SCHEME, GET THE APPROVAL OF THE DESIGN AUTHORITY." |
| amendment (n) | NOT APPROVED | use: CHANGE (n); CHANGE (v) |
| among (prep) | NOT APPROVED | use: IN (prep) — "If there are metal particles among the samples, replace the pump." → "IF THERE ARE METAL PARTICLES IN THE SAMPLES, REPLACE THE PUMP." |
| amount (n) | NOT APPROVED | use: QUANTITY (n) — "Make sure that the amount of fuel in the tank is not more than 500 liters." → "MAKE SURE THAT THE QUANTITY OF FUEL IN THE TANK IS NOT MORE THAN 500 LITERS." |
| AN (art) | Function word: indefinite article |  |
| ANALOG (adj) | Of data given by pointers and dials |  |
| analyze (v) | NOT APPROVED | use: ANALYSIS (TN) — "Analyze the oil sample." → "MAKE AN ANALYSIS OF THE OIL." |
| anchor (v) | NOT APPROVED | use: ATTACH (v) — "The straps are anchored to a full-length rail." → "THE STRAPS ARE ATTACHED TO A FULL-LENGTH RAIL." |
| ancillary (adj) | NOT APPROVED | use: AUXILIARY (adj); SECONDARY (adj) |
| AND (conj) | Function word used to connect words, phrases, or clauses |  |
| ANGULAR (adj) | That has one or more angles |  |
| annotation (n) | NOT APPROVED | use: WRITE (v); RECORD (v) |
| annunciate (v) | NOT APPROVED | use: SHOW (v) — "The display annunciates a fault message." → "THE DISPLAY SHOWS A FAULT MESSAGE." |
| another (adj) | NOT APPROVED | use: DIFFERENT (adj); AGAIN (adv) — ONE (TN) MORE |
| anticlockwise (adv) | NOT APPROVED | use: COUNTERCLOCKWISE (adv) — "Turn the cap anticlockwise." → "TURN THE CAP COUNTERCLOCKWISE." |
| any (adj) | NOT APPROVED | Frequently, an alternative for this word is not necessary. — "If you have any questions about this document, send an e-mail to the address that follows:" → "IF YOU HAVE QUESTIONS ABOUT THIS DOCUMENT, SEND AN E-MAIL TO THE ADDRESS THAT FOLLOWS:" |
| any (pron) | NOT APPROVED | use: ONE (TN) — "Remove any of the four bolts." → "REMOVE ONE OF THE FOUR BOLTS." |
| anytime (adv) | NOT APPROVED | use: WHEN (conj) — "Anytime you use the emergency pump, record the time of operation." → "WHEN YOU USE THE EMERGENCY PUMP, RECORD THE TIME OF OPERATION." |
| APART (adv) | At a distance (not specified) from |  |
| aperture (n) | NOT APPROVED | use: OPENING (n) — "Get access to the control unit through the aperture in the side of the tank." → "GET ACCESS TO THE CONTROL UNIT THROUGH THE OPENING IN THE SIDE OF THE TANK." |
| apparent (adj) | NOT APPROVED | use: SEE (v); FIND (v) |
| appear (v) | NOT APPROVED | use: SHOW (v); VIEW (n); THINK (v); POSSIBLE (adj) |
| APPLICABLE (adj) | Correct or satisfactory for the task |  |
| application (n) | NOT APPROVED | use: APPLY (v) — "The application of sealant must be carried out with a wooden spatula." → "APPLY THE SEALANT WITH A WOODEN SPATULA." |
| APPLY (v) | 1. To put or spread something on 2. To use something (for example, pressure, force, load) to cause an effect | forms: APPLIES, APPLIED, APPLIED |
| appoint (v) | NOT APPROVED | use: TELL (v) — "Appoint two persons to be prepared to operate the fire extinguishers." → "TELL TWO PERSONS TO BE PREPARED TO OPERATE THE FIRE EXTINGUISHERS." |
| approach (v) | NOT APPROVED | use: GO NEAR — "If it is necessary to approach the engine exhaust, use ear protection." → "IF IT IS NECESSARY TO GO NEAR THE ENGINE EXHAUST, USE EAR PROTECTION." |
| appropriate (adj) | NOT APPROVED | use: APPLICABLE (adj) — "Lock the washer with the appropriate tabs." → "LOCK THE WASHER WITH THE APPLICABLE TABS." |
| APPROVAL (n) | That which permits a person or a thing to do something |  |
| approve (v) | NOT APPROVED | use: APPROVAL (n) — "All modifications must be approved by the Design Authority." → "APPROVAL FROM THE DESIGN AUTHORITY IS MANDATORY FOR ALL MODIFICATIONS." |
| APPROVED (adj) | Permitted by an authority |  |
| APPROXIMATE (adj) | Almost correct or accurate |  |
| APPROXIMATELY (adv) | Almost correct or accurate |  |
| AREA (n) | A specified surface or location |  |
| arise (v) | NOT APPROVED | use: OCCUR (v); CAUSE (v) |
| ARM (v) | 1. To install armaments 2. To prepare for automatic operation | forms: ARMS, ARMED, ARMED |
| AROUND (prep) | On all sides of | For other meanings, use: APPROXIMATELY (adv) |
| arrange (v) | NOT APPROVED | use: PUT (v) — "Arrange the components in this order." → "PUT THE COMPONENTS IN THIS SEQUENCE:" |
| arrangement (n) | NOT APPROVED | use: CONFIGURATION (TN); PREPARE (v) |
| arrest (v) | NOT APPROVED | use: STOP (v); HOLD (v) |
| arrive (v) | NOT APPROVED | use: GET (v) — "To arrive at the correct value, set the switch to position 2." → "TO GET THE CORRECT VALUE, SET THE SWITCH TO POSITION 2." |
| ARROW (n) | A mark that has a point to show direction |  |
| article (n) | NOT APPROVED | use: OBJECT (n) — "Ensure that there are no loose articles in the engine air intakes." → "MAKE SURE THAT THERE ARE NO LOOSE OBJECTS IN THE ENGINE AIR INTAKES." |
| AS (prep) | In the manner of, to the same quantity, equally |  |
| as (conj) | NOT APPROVED | use: BECAUSE (conj); WHILE (conj) — You can use: AS FOLLOWS AS NECESSARY AS SHOWN |
| AS ... AS (conj) | Construction used to show comparison or relation For “as long as,” refer to “long (as long as).” |  |
| ascertain (v) | NOT APPROVED | use: MAKE SURE (v) — "Ascertain that the light is off." → "MAKE SURE THAT THE LIGHT IS OFF." |
| ask (v) | NOT APPROVED | use: TELL (v); SPEAK (v) |
| ASSEMBLE (v) | To attach, connect, or put together the parts of something | forms: ASSEMBLES, ASSEMBLED, ASSEMBLED |
| ASSEMBLY (n) | Items that are connected for a specified function |  |
| assess (v) | NOT APPROVED | use: CALCULATE (v); ESTIMATE (n) |
| assessment (n) | NOT APPROVED | use: ESTIMATE (n); CALCULATE (v) |
| assign (v) | NOT APPROVED | use: GIVE (v) — "Assign a code to each connector." → "GIVE A CODE TO EACH CONNECTOR." |
| assist (v) | NOT APPROVED | use: HELP (v) — "Keep the data to assist subsequent procedures." → "KEEP THE DATA TO HELP YOU WITH SUBSEQUENT PROCEDURES." |
| assistance (n) | NOT APPROVED | use: AID (n); HELP (v) |
| associated (adj) | NOT APPROVED | use: CORRECT (adj); RELATED (adj); ITS (adj); THEIR (adj) |
| assume (v) | NOT APPROVED | use: THINK (v) — "If damage is assumed to be repairable, refer to the repair section." → "IF YOU THINK THAT YOU CAN REPAIR THE DAMAGE, REFER TO THE REPAIR SECTION." |
| assure (v) | NOT APPROVED | use: MAKE SURE (v) — "Use a plumb line to assure that the wall is vertical." → "USE A PLUMB LINE TO MAKE SURE THAT THE WALL IS VERTICAL." |
| as to (prep) | NOT APPROVED | use: ABOUT (prep) — "Refer to Table 7001 for information as to the construction of the pivot assembly." → "REFER TO TABLE 7001 FOR INFORMATION ABOUT HOW THE PIVOT ASSEMBLY IS MADE." |
| asymmetric (adj) | NOT APPROVED | use: NOT SYMMETRICAL — "If you get an asymmetric result, do a rigging test." → "IF THE RESULT THAT YOU GET IS NOT SYMMETRICAL, DO A RIGGING TEST." |
| AT (prep) | Function word that shows the location, position, direction, or time that something occurs |  |
| ATTACH (v) | To stay together or to cause different items to stay together | forms: ATTACHES, ATTACHED, ATTACHED |
| attachment (n) | NOT APPROVED | use: ATTACH (v) — "Make sure that the attachment of the duct to the filter is correct." → "MAKE SURE THAT THE DUCT IS CORRECTLY ATTACHED TO THE FILTER." |
| attain (v) | NOT APPROVED | use: SHOW (v); BE (v); GET (v) |
| attempt (n) | NOT APPROVED | use: TRY (v) — "Make an attempt to lift the cover manually." → "TRY TO LIFT THE COVER MANUALLY." |
| attempt (v) | NOT APPROVED | use: TRY (v) — "Attempt to find the defect." → "TRY TO FIND THE DEFECT." |
| attention (n) | NOT APPROVED | use: AID (n); CAREFUL (adj); MONITOR (v) |
| audible (adj) | NOT APPROVED | use: HEAR (v); LISTEN (v) |
| augment (v) | NOT APPROVED | use: INCREASE (v) — "A mixture of water and methanol augments the power of the engine." → "A MIXTURE OF WATER AND METHANOL INCREASES THE POWER OF THE ENGINE." |
| aurally (adv) | NOT APPROVED | use: LISTEN (v); HEAR (v) |
| authentic (adj) | NOT APPROVED | use: ACCURATE (adj) — "If the adjustment of the stops is not correct, the results of the test will not be authentic." → "IF THE ADJUSTMENT OF THE STOPS IS NOT CORRECT, THE RESULTS OF THE TEST WILL NOT BE ACCURATE." |
| AUTHORITY (n) | An official organization that gives approval to something |  |
| authorized (adj) | NOT APPROVED | use: APPROVED (adj) — "Only authorized persons are permitted to stay in this area." → "ONLY APPROVED PERSONS ARE PERMITTED TO STAY IN THIS AREA." |
| AUTOMATIC (adj) | That operates without other input |  |
| AUTOMATICALLY (adv) | That operates without other input |  |
| AUXILIARY (adj) | 1. That operates in a secondary function 2. That gives help |  |
| AVAILABLE (adj) | Prepared or supplied for you to use |  |
| avert (v) | NOT APPROVED | use: PREVENT (v) — "If the microswitch becomes unserviceable, deactivate the actuator to avert damage to the valve." → "IF THE MICROSWITCH BECOMES UNSERVICEABLE, DEACTIVATE THE ACTUATOR TO PREVENT DAMAGE TO THE VALVE." |
| avoid (v) | NOT APPROVED | use: PREVENT (v); DO NOT |
| aware (adj) | NOT APPROVED | use: KNOW (v); TELL (v) |
| AWAY FROM (prep) | In or to a different position or direction |  |
| AXIAL (adj) | Related to an axis |  |
| AXIALLY (adv) | Related to an axis |  |
| back (adj) | NOT APPROVED | use: REAR (adj) — "Disconnect the cable from the back side of the instrument." → "DISCONNECT THE CABLE FROM THE REAR SIDE OF THE INSTRUMENT." |
| BACK (adv) | To an initial condition |  |
| back (n) | NOT APPROVED | use: REAR (n) — "The control unit is at the back." → "THE CONTROL UNIT IS AT THE REAR." |
| back and forth (adv) | NOT APPROVED | use: DIRECTION (n) — "Move the sleeve back and forth in the piston." → "MOVE THE SLEEVE IN THE PISTON TO ONE DIRECTION AND THEN BACK AGAIN." |
| back off (v) | NOT APPROVED | use: LOOSEN (v) — "Do not back off the nut to obtain alignment." → "DO NOT LOOSEN THE NUT TO ALIGN IT." |
| backup (n) | NOT APPROVED | use: EMERGENCY (n); AUXILIARY (adj) |
| backward (adv) | NOT APPROVED | use: REARWARD (adv) — "Move the lever backward." → "MOVE THE LEVER REARWARD." |
| BAD (adj) | Not satisfactory | Do not use this word if more accurate and clear words are available.; forms: (WORSE, WORST) |
| badly (adv) | NOT APPROVED | use: INCORRECTLY (adv); UNSATISFACTORILY (adv); DECREASE (v) |
| BALANCE (v) | To make equal | forms: BALANCES, BALANCED, BALANCED |
| bank (v) | NOT APPROVED | use: BANK (TN) — "The V-BARS indicate the command to bank." → "THE V-BARS GIVE THE INDICATION FOR A BANK." |
| BARE (adj) | Without a surface layer or protection |  |
| bared (adj) | NOT APPROVED | use: BARE (adj) — "Give temporary protection to areas of bared metal." → "GIVE TEMPORARY PROTECTION TO AREAS OF BARE METAL." |
| base (n) | NOT APPROVED | use: BOTTOM (n) — "Make sure that the two spigots at the base of the unit engage." → "MAKE SURE THAT THE TWO SPIGOTS AT THE BOTTOM OF THE UNIT ENGAGE." |
| base (v) | NOT APPROVED | use: USE (v) — "Base the torque values on those given in Chapter 10." → "USE THE TORQUE VALUES GIVEN IN CHAPTER 10." |
| BASIC (adj) | Approved minimum |  |
| BE (v) | 1. To occur, exist 2. To have a property, to be equal to | forms: IS, WAS, (also ARE, WERE) No other verb forms. |
| BECAUSE (conj) | As a result of |  |
| BECAUSE OF (prep) | As a result of |  |
| BECOME (v) | To come to be | forms: BECOMES, BECAME No other verb forms. |
| BEFORE (conj) | That precedes a specified time, sequence, or operation |  |
| BEFORE (prep) | That precedes a specified time, sequence, or operation |  |
| begin (v) | NOT APPROVED | use: START (v) — "Increase pressure until the flow begins again." → "INCREASE THE PRESSURE UNTIL THE FLOW STARTS AGAIN." |
| beginning (n) | NOT APPROVED | use: START (n); SOURCE (n); START (v) |
| BEHIND (prep) | In a position at the rear of |  |
| below (adv) | NOT APPROVED | use: FOLLOW (v); THESE (adj) |
| BELOW (prep) | In (or to) a position farther down than something | For other meanings, use: LESS THAN |
| BEND (n) | The area where something is bent |  |
| BEND (v) | To change or cause to change from straight to curved | forms: BENDS, BENT, BENT |
| beneath (prep) | NOT APPROVED | use: BELOW (prep) — "Put the jack beneath the axle." → "PUT THE JACK BELOW THE AXLE." |
| beside (prep) | NOT APPROVED | use: ADJACENT TO — "The fuel pump is beside the structural support." → "THE FUEL PUMP IS ADJACENT TO THE STRUCTURAL SUPPORT." |
| BETWEEN (prep) | Related to something before and after in time or position |  |
| beware (v) | NOT APPROVED | use: CAREFUL (adj) — "Beware of dangerous voltages." → "BE CAREFUL OF DANGEROUS VOLTAGES." |
| beyond (prep) | NOT APPROVED | use: MORE THAN — "Replace all components that are worn beyond their maximum limits." → "REPLACE ALL COMPONENTS THAT ARE WORN MORE THAN THE MAXIMUM LIMITS." |
| big (adj) | NOT APPROVED | use: LARGE (adj) — If it is possible, give an accurate value. — "Install the bigger bolts." → "INSTALL THE LARGER BOLTS." |
| bind (v) | NOT APPROVED | use: FREELY (adv); WIND AROUND |
| blank (v) | NOT APPROVED | use: SEAL (v); CAP (TN); COVER (TN) |
| BLEED (v) | To let a gas out of | forms: BLEEDS, BLED, BLED |
| blend (v) | NOT APPROVED | use: MIX (v) — "Blend the adhesive with the hardener." → "MIX THE ADHESIVE WITH THE HARDENER." |
| block (v) | NOT APPROVED | use: CAUSE A BLOCKAGE — "Check that the sealant does not block the drain." → "MAKE SURE THAT THE SEALANT DOES NOT CAUSE A BLOCKAGE OF THE DRAIN." |
| BLOCKAGE (n) | That which prevents correct operation |  |
| BLOCKED (adj) | That prevents correct operation |  |
| blot (v) | NOT APPROVED | use: DRY (v) — "Blot the surface with a towel." → "DRY THE SURFACE WITH A TOWEL." |
| BLOW (v) | To cause gas to move | forms: BLOWS, BLEW, BLOWN |
| BLUNT (adj) | Not sharp |  |
| blunted (adj) | NOT APPROVED | use: BLUNT (adj) — "Inspect the static dischargers for bent and blunted pins." → "EXAMINE THE STATIC DISCHARGERS FOR BENT AND BLUNT PINS." |
| bolt (v) | NOT APPROVED | use: ATTACH (v) — (WITH A BOLT [TN] OR BOLTS [TN]) — "Bolt the track to the channels." → "ATTACH THE TRACK TO THE CHANNELS WITH THE BOLTS." |
| BOND (n) | 1. A connection between structural components for electrical continuity 2. A firm connection with another material |  |
| BOND (v) | 1. To make an electrical bond 2. To attach firmly or become firmly attached with another material | forms: BONDS, BONDED, BONDED |
| both (adj) | NOT APPROVED | use: THE TWO (TN) — "Attach both ends of the hose." → "ATTACH THE TWO ENDS OF THE HOSE." |
| BOTTOM (adj) | That is lowermost |  |
| BOTTOM (n) | The lowermost position |  |
| bottom (v) | NOT APPROVED | use: TOUCH (v) — "Open the door until it bottoms on the floor." → "OPEN THE DOOR UNTIL IT TOUCHES THE FLOOR." |
| bounds (n) | NOT APPROVED | use: LIMIT (n) — "Make sure that the clearance is in bounds." → "MAKE SURE THAT THE CLEARANCE IS IN THE LIMITS." |
| brace (v) | NOT APPROVED | use: HOLD (v); STRONG (adj) |
| branch (v) | NOT APPROVED | use: DIVIDE (v) — "The pressure lines branch in different directions." → "THE PRESSURE LINES DIVIDE IN DIFFERENT DIRECTIONS." |
| breadth (n) | NOT APPROVED | use: WIDTH (n) — "The breadth of the material must be larger than 10 mm." → "THE WIDTH OF THE MATERIAL MUST BE LARGER THAN 10 mm." |
| break (n) | NOT APPROVED | use: STOP (v) — "If there is a break in the transmission, cancel the test." → "IF THE TRANSMISSION STOPS, CANCEL THE TEST." |
| BREAK (v) | To cause to separate or become separated into parts by force | forms: BREAKS, BROKE, BROKEN |
| breakdown (n) | NOT APPROVED | use: STOP (v) — "If there is a breakdown in the pressure supply, cancel the test." → "IF THE PRESSURE SUPPLY STOPS, CANCEL THE TEST." |
| BREATHE (v) | To get gas into or out of the lungs | forms: BREATHES, BREATHED, BREATHED |
| BRIGHT (adj) | That gives much light | forms: (BRIGHTER, BRIGHTEST) |
| BRIGHTLY (adv) | In a bright manner |  |
| brilliance (n) | NOT APPROVED | use: INTENSITY (n); BRIGHT (adj) |
| bring (v) | NOT APPROVED | use: MOVE (v); PUT (v) |
| briskly (adv) | NOT APPROVED | use: QUICKLY (adv) — "Rub the surface briskly with a soft, dry cloth." → "RUB THE SURFACE QUICKLY WITH A SOFT, DRY CLOTH." |
| broadcast (v) | NOT APPROVED | use: TRANSMIT (v) — "Broadcast the data on both channels." → "TRANSMIT THE DATA ON THE TWO CHANNELS." |
| brush (v) | NOT APPROVED | use: BRUSH (TN) — "Brush the filter element to clean it. Brush the filter element to clean it." → "CLEAN THE FILTER ELEMENT WITH A BRUSH. USE A BRUSH TO CLEAN THE FILTER ELEMENT." |
| brush on (v) | NOT APPROVED | use: BRUSH (TN) — "Brush the paint on." → "APPLY THE PAINT WITH A BRUSH." |
| BUBBLE (n) | A small quantity of gas in a liquid or a solid |  |
| build (n) | NOT APPROVED | use: STRUCTURE (n) — "The build of the wing allows maximum fuel storage." → "THE WING STRUCTURE GIVES MAXIMUM FUEL CAPACITY." |
| build (v) | NOT APPROVED | use: ASSEMBLE (v) — "Build the unit." → "ASSEMBLE THE UNIT." |
| bump (v) | NOT APPROVED | use: HIT (v) — "The fueling hose must not bump the edge of the tank." → "THE FUELING HOSE MUST NOT HIT THE EDGE OF THE TANK." |
| BURN (v) | 1. To cause or undergo combustion 2. To cause injury or damage through heat | forms: BURNS, BURNED, BURNED |
| burst (v) | NOT APPROVED | use: BREAK (v) — "If the disk bursts, switch off the supply." → "IF THE DISK BREAKS, STOP THE SUPPLY." |
| BUT (conj) | On the contrary |  |
| butt (v) | NOT APPROVED | use: TOUCH (v) — "The wire must butt against the rear of the contact." → "THE WIRE MUST TOUCH THE REAR OF THE CONTACT." |
| BY (prep) | Mathematical function word |  |
| by means of (prep) | NOT APPROVED | use: WITH (prep) — "By means of the hand pump, pressurize the system to 150 bar." → "PRESSURIZE THE SYSTEM TO 150 bar WITH THE HAND PUMP." |
| BYPASS (v) | To change a circuit so that it goes past something instead of through it | forms: BYPASSES, BYPASSED, BYPASSED |
| CALCULATE (v) | To find a result by mathematics | forms: CALCULATES, CALCULATED, CALCULATED |
| calculation (n) | NOT APPROVED | use: CALCULATE (v) — "Data from the system calculations apply only to a Type B unit." → "THE SYSTEM CALCULATES DATA THAT ARE APPLICABLE ONLY TO A TYPE B UNIT." |
| CALIBRATE (v) | To measure and adjust the precision of something | forms: CALIBRATES, CALIBRATED, CALIBRATED |
| CALIBRATION (n) | The procedure that calibrates |  |
| call (v) | NOT APPROVED | use: TELL (v) — "Call the ramp agent to remove the chocks." → "TELL THE RAMP AGENT TO REMOVE THE CHOCKS." |
| CAN (v) | Auxiliary modal verb that means to be possible, to be able to, or to be permitted to | Do not use COULD (v) to show possibility; forms: CAN, COULD No other verb forms. |
| CANCEL (v) | 1. To do the necessary steps to stop a process 2. To remove the validity of something | forms: CANCELS, CANCELED, CANCELED |
| CANNOT (v) | Auxiliary modal verb that means to not be able to |  |
| cap (v) | NOT APPROVED | use: SEAL (v); CAP (TN); COVER (TN) |
| capability (n) | NOT APPROVED | use: FUNCTION (n); CAN (v) |
| capable (adj) | NOT APPROVED | use: APPROVED (adj); CAN (v) |
| CAPACITY (n) | The maximum quantity that something can hold or make |  |
| care (n) | NOT APPROVED | use: PRECAUTION (n); CAREFUL (adj); CAREFULLY (adv) |
| CAREFUL (adj) | With precaution |  |
| CAREFULLY (adv) | In a careful manner |  |
| carry (v) | NOT APPROVED | use: TRANSMIT (v); TRANSPORT (TN) |
| carry out (v) | NOT APPROVED | use: DO (v); MEASURE (v) — You can use a more accurate command verb. |
| case (n) | NOT APPROVED | use: CONDITION (n) — "The data for all operational cases are shown in Figure 1." → "FIGURE 1 SHOWS THE DATA FOR ALL OPERATIONAL CONDITIONS." |
| case (in case of) (conj) | NOT APPROVED | use: IF (conj) — "In case of a fire, operate the crash switches." → "IF THERE IS A FIRE, OPERATE THE CRASH SWITCHES." |
| CATCH (v) | To stop or prevent the movement of something | For other meanings, use: COLLECT (v); forms: CATCHES, CAUGHT, CAUGHT |
| categorize (v) | NOT APPROVED | use: CATEGORY (TN) — "The testing equipment categorizes the faults." → "THE TESTING EQUIPMENT DIVIDES THE FAULTS INTO CATEGORIES." |
| CAUSE (n) | Something that brings about a result |  |
| CAUSE (v) | To be the cause of | forms: CAUSES, CAUSED, CAUSED |
| caution (v) | NOT APPROVED | use: TELL (v) — "Caution all personnel not to smoke near fuel tanks." → "TELL ALL PERSONNEL NOT TO SMOKE NEAR FUEL TANKS." |
| cautiously (adv) | NOT APPROVED | use: CAREFULLY (adv) — "Cautiously feel the heater with your hands to make sure that it operates." → "CAREFULLY FEEL THE HEATER WITH YOUR HANDS TO MAKE SURE THAT IT OPERATES." |
| cavity (n) | NOT APPROVED | use: HOLE (n); SPACE (n) |
| cease (v) | NOT APPROVED | use: STOP (v) — "The warning ceases at 17 deg." → "THE WARNING STOPS AT 17 DEG." |
| center (v) | NOT APPROVED | use: CENTER (TN) — "Center the piston in the sleeve." → "ALIGN THE PISTON WITH THE CENTER OF THE SLEEVE." |
| centralize (v) | NOT APPROVED | use: CENTER (TN) — "Centralize the controls." → "SET THE CONTROLS TO THE CENTER POSITION." |
| certain (adj) | NOT APPROVED | use: SURE (adj); SOME (adj); SPECIFIED (adj) |
| certify (v) | NOT APPROVED | use: WRITE (v); APPROVAL (n) |
| chafe (v) | NOT APPROVED | use: RUB (v) — "Do not let the wires chafe." → "DO NOT LET THE WIRES RUB." |
| chafed (adj) | NOT APPROVED | use: WORN (adj) — "Examine the tubing for chafed areas." → "EXAMINE THE TUBING FOR WORN AREAS." |
| chance (by chance) (n) | NOT APPROVED | use: RISK (n); ACCIDENTALLY (adv) |
| CHANGE (n) | That which occurs when something changes |  |
| CHANGE (v) | To become or to cause to become different | For other meanings, use: REPLACE (v); forms: CHANGES, CHANGED, CHANGED |
| channel (v) | NOT APPROVED | use: CHANNEL (TN) — "Channel the wires along the housing." → "INSTALL THE WIRES IN THE CHANNEL ALONG THE HOUSING." |
| characteristic (n) | NOT APPROVED | use: PROPERTY (n); QUALITY (n) |
| CHARGE (v) | To accumulate or add electrical energy | For other meanings, use: FILL (v); PRESSURIZE (v); forms: CHARGES, CHARGED, CHARGED |
| CHECK (n) | The procedure you do to make sure that something operates correctly or has no defects |  |
| check (v) | NOT APPROVED | use: MAKE SURE (v); MEASURE (v); EXAMINE (v); CHECK (n) |
| CHEMICAL (adj) | Related to a chemical |  |
| CHEMICALLY (adv) | Related to a chemical |  |
| chip (n) | NOT APPROVED | use: PARTICLE (n) — "Examine the filter element for metal chips." → "EXAMINE THE FILTER ELEMENT FOR METAL PARTICLES." |
| chip (v) | NOT APPROVED | use: DAMAGED (adj) — "If the enamel is chipped, replace the unit." → "IF THE ENAMEL IS DAMAGED, REPLACE THE UNIT." |
| chock (v) | NOT APPROVED | use: CHOCK (TN) — "Chock the wheels." → "PUT CHOCKS AGAINST THE WHEELS." |
| choice (n) | NOT APPROVED | use: SELECTION (n); ALTERNATIVE (adj) |
| choose (v) | NOT APPROVED | use: SELECT (v); ALTERNATIVE (adj) |
| circa (prep) | NOT APPROVED | use: APPROXIMATELY (adv) — "Put a container (circa 5 liters) under the waste water outlet." → "PUT A CONTAINER (APPROXIMATELY 5 LITERS) BELOW THE WASTE WATER OUTLET." |
| circle (v) | NOT APPROVED | use: AROUND (prep) — "The pointer circles the dial." → "THE POINTER MOVES AROUND THE DIAL." |
| CIRCULAR (adj) | That has the shape of a circle |  |
| circulate (v) | NOT APPROVED | use: SUPPLY (v) — "Circulate air at 24 °C in the area." → "SUPPLY AIR AT 24 °C TO THE AREA." |
| clamp (v) | NOT APPROVED | use: ATTACH (v); PUT (v) — (WITH A CLAMP [TN] OR CLAMPS [TN]) (A CLAMP [TN] OR CLAMPS [TN]) |
| classification (n) | NOT APPROVED | use: CLASS (TN); CATEGORY (TN) |
| CLEAN (adj) | That does not include dirt or unwanted material |  |
| CLEAN (v) | To remove dirt or unwanted materials | forms: CLEANS, CLEANED, CLEANED |
| cleanliness (n) | NOT APPROVED | use: CLEAN (adj) — "A satisfactory bond depends on the cleanliness of the surface, the temperature, and the pressure." → "CONDITIONS FOR A SATISFACTORY BOND ARE: - A CLEAN SURFACE - A CORRECT TEMPERATURE - A CORRECT PRESSURE." |
| CLEAR (adj) | 1. Without blockage or interference 2. Easy to understand and without ambiguity | For other meanings, use: TRANSPARENT (adj) |
| clear (v) | NOT APPROVED | use: CLEAN (v) — You can also use a different construction. — "Clear the drain hole. Lift the seat so that it clears the track locks." → "CLEAN THE DRAIN HOLE. LIFT THE SEAT UNTIL IT IS AWAY FROM THE TRACK LOCKS." |
| CLEARANCE (n) | The space between two objects that must be clear to make sure that they do not touch |  |
| CLEARLY (adv) | In a clear and not ambiguous manner |  |
| CLICK (n) | A short, sharp sound |  |
| click (v) | NOT APPROVED | use: CLICK (n) — "When the solenoid clicks, the valve is open." → "WHEN THE SOLENOID MAKES A CLICK, THE VALVE IS OPEN." |
| clip (v) | NOT APPROVED | use: CUT (v); ATTACH (v) — (WITH A CLIP [TN] OR CLIPS [TN]) |
| CLOCKWISE (adv) | In the direction in which the hands of a clock turn when seen from the front |  |
| CLOGGED (adj) | Blocked with unwanted material. |  |
| close (adj) | NOT APPROVED | use: NEAR (prep) — "Do not use solvents in close contact with flames or sparks." → "DO NOT USE SOLVENTS NEAR FLAMES OR SPARKS." |
| CLOSE (v) | 1. To move together, or to move to a position that stops or prevents materials from going in or out 2. To operate a circuit breaker to make an electrical circuit | forms: CLOSES, CLOSED, CLOSED |
| closely (adv) | NOT APPROVED | use: CAREFULLY (adv) — "Closely monitor the operation of the system." → "CAREFULLY MONITOR THE OPERATION OF THE SYSTEM." |
| close to (adv) | NOT APPROVED | use: NEAR (prep) — "Put the clinometer close to the fuselage centerline." → "PUT THE CLINOMETER NEAR THE FUSELAGE CENTERLINE." |
| coat (n) | NOT APPROVED | use: LAYER (n) — "Spread a coat of sealant PR 1440 B2 on the surface." → "APPLY A LAYER OF SEALANT PR 1440 B2 ON THE SURFACE." |
| coat (v) | NOT APPROVED | use: LAYER (n) — "Coat the battery cables with grease." → "APPLY A LAYER OF GREASE TO THE BATTERY CABLES." |
| coating (n) | NOT APPROVED | use: LAYER (n) — "The metal has a coating of plastic on it to prevent corrosion." → "THE METAL HAS A LAYER OF PLASTIC ON IT TO PREVENT CORROSION." |
| cock (v) | NOT APPROVED | use: SET (v) — "Cock the rack hooks." → "SET THE RACK HOOKS." |
| CODE (n) | A sequence of symbols, letters, and/or numbers used for identification |  |
| code (v) | NOT APPROVED | use: IDENTIFY (v); CODE (n) |
| COIL (n) | A sequence of loops |  |
| coil (v) | NOT APPROVED | use: WIND (v) — "Coil the cables carefully." → "WIND THE CABLES CAREFULLY." |
| coincide (v) | NOT APPROVED | use: ALIGN (v) — "The fasteners must coincide with the holes in the track." → "THE FASTENERS MUST ALIGN WITH THE HOLES IN THE TRACK." |
| coincident (adj) | NOT APPROVED | use: SYNCHRONIZED (adj); ALIGN (v) |
| COLD (adj) | At low temperature | forms: (COLDER, COLDEST) |
| collapse (v) | NOT APPROVED | use: CLOSE (v); FALL (v) |
| COLLECT (v) | To come, or cause to come, together in one location | forms: COLLECTS, COLLECTED, COLLECTED |
| COLOR (n) | A property of light |  |
| color code (v) | NOT APPROVED | use: IDENTIFY (v); CODE (n) |
| colored (adj) | NOT APPROVED | use: COLOR (n) — "The scale is divided into two colored areas." → "THE SCALE HAS TWO AREAS OF DIFFERENT COLOR." |
| combine (v) | NOT APPROVED | use: MIX (v); PUT TOGETHER |
| combustible (adj) | NOT APPROVED | use: FLAMMABLE (adj) — "Keep combustible materials at a minimum distance of 50 feet from the work area." → "KEEP FLAMMABLE MATERIALS AT A MINIMUM DISTANCE OF 50 FEET FROM THE WORK AREA." |
| COME (v) | To move to your location | forms: COMES, CAME No other verb forms. |
| COME ON (v) | To become bright with light when an internal power source is energized | forms: COMES ON, CAME ON No other verb forms. |
| commence (v) | NOT APPROVED | use: START (v) — "The warning commences and the indicators flash." → "THE WARNING STARTS AND THE INDICATORS FLASH." |
| commencement (n) | NOT APPROVED | use: START (v) — "After the test commencement, monitor the results on the screen." → "AFTER THE TEST STARTS, MONITOR THE RESULTS ON THE SCREEN." |
| common (adj) | NOT APPROVED | use: SAME (adv) — "The removal procedure is common to both items." → "THE REMOVAL PROCEDURE IS THE SAME FOR THE TWO ITEMS." |
| communicate (v) | NOT APPROVED | use: CONTACT (v); SPEAK (v); HEAR (v); COMMUNICATION (n) |
| COMMUNICATION (n) | The exchange of information through a common system of symbols, signs, or sounds |  |
| COMPARE (v) | To examine for differences | forms: COMPARES, COMPARED, COMPARED |
| comparison (n) | NOT APPROVED | use: COMPARE (v) — "Make a comparison of the two readings." → "COMPARE THE TWO INDICATIONS." |
| COMPATIBLE (adj) | That can operate together satisfactorily or be used together safely |  |
| compile (v) | NOT APPROVED | use: MAKE A LIST; RECORD (v); COLLECT (v) |
| complete (adj) | NOT APPROVED | use: FULL (adj); ALL (adj); COMPLETED (adj) |
| COMPLETE (v) | To bring to an end | forms: COMPLETES, COMPLETED, COMPLETED |
| COMPLETED (adj) | Successfully brought to an end |  |
| completely (adv) | NOT APPROVED | use: FULLY (adv) — "Allow the first layer of paint to dry completely before applying the second layer." → "BEFORE YOU APPLY THE SECOND LAYER, LET THE FIRST LAYER OF PAINT DRY FULLY." |
| completion (n) | NOT APPROVED | use: END (n); COMPLETE (v) |
| complicated (adj) | NOT APPROVED | use: NOT EASY — "This test procedure is complicated without the right equipment." → "THIS TEST PROCEDURE IS NOT EASY WITHOUT THE CORRECT EQUIPMENT." |
| comply (v) | NOT APPROVED | use: OBEY (v) — Used in law and regulations. Refer to rule 1.12. — "When you assemble the unit, comply with this procedure." → "WHEN YOU ASSEMBLE THE UNIT, OBEY THIS PROCEDURE. THE SHIP CERTIFICATE MUST COMPLY WITH ALL THE REQUIREMENTS OF THE AUTHORITIES." |
| COMPONENT (n) | A part, subassembly, or unit that has a specified function |  |
| comprehensive (adj) | NOT APPROVED | use: FULL (adj) — "Do a comprehensive inspection of the fairing." → "DO A FULL INSPECTION OF THE FAIRING." |
| COMPRESS (v) | To decrease or cause to decrease in dimension or volume | forms: COMPRESSES, COMPRESSED, COMPRESSED |
| comprise (v) | NOT APPROVED | use: HAVE (v); CONTAIN (v) |
| compulsory (adj) | NOT APPROVED | use: MANDATORY (adj) — "Before you install a new component, it is compulsory to replace the filter." → "BEFORE YOU INSTALL A NEW COMPONENT, IT IS MANDATORY TO REPLACE THE FILTER." |
| compute (v) | NOT APPROVED | use: CALCULATE (v) — "Compute the voltage in the circuit." → "CALCULATE THE VOLTAGE IN THE CIRCUIT." |
| concentrate (v) | NOT APPROVED | use: ALL (adj) — "The weight must be concentrated on the spar tip." → "ALL THE WEIGHT MUST BE ON THE SPAR TIP." |
| CONCENTRATION (n) | The strength of something contained in a mixture |  |
| CONCENTRIC (adj) | That has a common center |  |
| concern (v) | NOT APPROVED | use: APPLICABLE (adj) — "This procedure only concerns a Type B unit." → "THIS PROCEDURE IS APPLICABLE ONLY TO A TYPE B UNIT." |
| conclusion (n) | NOT APPROVED | use: END (n); RESULT (n) |
| concurrently (adj) | NOT APPROVED | use: AT THE SAME TIME — "These two procedures must be applied concurrently." → "DO THESE TWO PROCEDURES AT THE SAME TIME." |
| CONDENSATION (n) | The result when a gas changes into a liquid |  |
| CONDITION (n) | 1. Something that is necessary for what occurs 2. The state of an item Use IF (conj) for “on the condition that.” |  |
| conduct (v) | NOT APPROVED | use: DO (v) — "Conduct the leak test." → "DO THE LEAK TEST." |
| confine to (v) | NOT APPROVED | use: ONLY (adv) — "If the damage is confined to the middle treads, the tire is serviceable." → "IF THE DAMAGE IS ONLY TO THE MIDDLE TREADS, THE TIRE IS SERVICEABLE." |
| confirm (v) | NOT APPROVED | use: MAKE SURE (v) — "Do a ground run of the engine to confirm the indications." → "DO A GROUND RUN OF THE ENGINE TO MAKE SURE THAT YOU GET THE SAME INDICATIONS." |
| conflict (n) | NOT APPROVED | use: DIFFERENT (adj); AGREE (v) |
| conform (v) | NOT APPROVED | use: AGREE (v) — "If the flap extension does not conform to the setting of the flap control lever, do the rigging procedure again." → "IF THE FLAP EXTENSION DOES NOT AGREE WITH THE POSITION OF THE FLAP CONTROL LEVER, DO THE RIGGING PROCEDURE AGAIN." |
| conformance (n) | NOT APPROVED | use: AGREE (v) — "The indications must be in conformance with those in Table 2." → "THE INDICATIONS MUST AGREE WITH THOSE IN TABLE 2." |
| conformity (n) | NOT APPROVED | use: AGREE (v) — "The accuracy of the gauges must be in conformity with the applicable quality standard." → "THE PRECISION OF THE GAUGES MUST AGREE WITH THE APPLICABLE QUALITY STANDARD." |
| CONNECT (v) | To come together or cause to come together to make one unit or system | forms: CONNECTS, CONNECTED, CONNECTED |
| CONNECTION (n) | That which connects or is connected |  |
| consecutive (adj) | NOT APPROVED | use: OTHER — ONE (TN) AFTER THE — "Do not do more than three consecutive starts." → "DO NOT DO MORE THAN THREE STARTS, ONE AFTER THE OTHER." |
| consecutively (adv) | NOT APPROVED | use: OTHER; SEQUENCE (n) — ONE (TN) AFTER THE |
| consequence (n) | NOT APPROVED | use: BECAUSE OF (prep) — "As a consequence of this defect, the unit will not operate." → "BECAUSE OF THIS DEFECT, THE UNIT WILL NOT OPERATE." |
| consider (v) | NOT APPROVED | use: THINK (v) — "If you consider that the indication is not correct, do the test again." → "IF YOU THINK THAT THE INDICATION IS NOT CORRECT, DO THE TEST AGAIN." |
| considerable (adj) | NOT APPROVED | use: LARGE (adj); IMPORTANT (adj); DANGEROUS (adj) |
| consist of (v) | NOT APPROVED | use: HAVE (v) — "Each antenna consists of three parts." → "EACH ANTENNA HAS THREE PARTS." |
| consistent (adj) | NOT APPROVED | use: AGREE (v) — "Check that the indications are consistent with the position of the flaps." → "MAKE SURE THAT THE INDICATIONS AGREE WITH THE POSITION OF THE FLAPS." |
| CONSTANT (adj) | That continues to be the same, without change |  |
| CONSTANTLY (adv) | Incessantly |  |
| construct (v) | NOT APPROVED | use: ASSEMBLE (v) — "Construct the unit." → "ASSEMBLE THE UNIT." |
| consult (v) | NOT APPROVED | use: REFER (v) — "For more information, consult the User’s Manual." → "FOR MORE INFORMATION, REFER TO THE USER’S MANUAL." |
| CONTACT (v) | To start communication | For other meanings, use: TOUCH (v); forms: CONTACTS, CONTACTED, CONTACTED |
| CONTAIN (v) | To have in something or hold in something | forms: CONTAINS, CONTAINED, CONTAINED |
| CONTAINER (n) | Something that holds fluids, materials, or objects |  |
| contaminant (n) | NOT APPROVED | use: CONTAMINATION (n) — "This filter removes all contaminants from the air supply." → "THIS FILTER REMOVES ALL CONTAMINATION FROM THE AIR SUPPLY." |
| contaminated (adj) | NOT APPROVED | use: DIRTY (adj); CONTAMINATION (n) |
| CONTAMINATION (n) | Unwanted change of the original condition of a material because of chemical or physical agents or a material that causes such a change |  |
| CONTENTS (n) | Something that is in a container |  |
| contiguous (adj) | NOT APPROVED | use: ADJACENT (adj) — "Remove the sensor to get access to the contiguous structure." → "REMOVE THE SENSOR TO GET ACCESS TO THE ADJACENT STRUCTURE." |
| CONTINUE (v) | To stay or keep in current condition or operation | forms: CONTINUES, CONTINUED, CONTINUED |
| CONTINUOUS (adj) | That continues |  |
| CONTINUOUSLY (adv) | In a continuous manner |  |
| CONTOUR (n) | The outer line of something |  |
| CONTROL (n) | Something that controls |  |
| CONTROL (v) | To give or send signals that adjust, operate, or keep something to a limit, or that cause something to operate | forms: CONTROLS, CONTROLLED, CONTROLLED |
| conventional (adj) | NOT APPROVED | use: STANDARD (adj) — "Pull the vehicle to a safe location where more conventional procedures can be applied." → "PULL THE VEHICLE TO A SAFE AREA WHERE YOU CAN USE THE STANDARD PROCEDURES." |
| converse (adj) | NOT APPROVED | use: OPPOSITE (adj) — "The reset device operates in the converse direction." → "THE RESET DEVICE OPERATES IN THE OPPOSITE DIRECTION." |
| convert (v) | NOT APPROVED | use: CHANGE (v) — "Convert the fuel load to U.S. gallons." → "CHANGE THE UNITS FOR THE FUEL LOAD TO U.S. GALLONS." |
| convey (v) | NOT APPROVED | use: MOVE (v); TELL (v) |
| COOL (adj) | Moderately cold |  |
| cool (v) | NOT APPROVED | use: DECREASE (v); COOL (adj) |
| coordinate (v) | NOT APPROVED | use: SYNCHRONIZED (adj) — "Coordinate compass system 1 and compass system 2." → "MAKE SURE THAT COMPASS SYSTEM 1 AND COMPASS SYSTEM 2 ARE SYNCHRONIZED." |
| COPY (n) | An object made the same as another object |  |
| copy (v) | NOT APPROVED | use: WRITE (v); COPY (n); RECORD (v) |
| CORNER (n) | The point or the angle made when lines, sides, or edges touch |  |
| CORRECT (adj) | That agrees with all that is necessary to the maximum |  |
| CORRECT (v) | To make correct | forms: CORRECTS, CORRECTED, CORRECTED |
| CORRECTION (n) | A change to make something correct |  |
| CORRECTLY (adv) | In a correct manner |  |
| correctness (n) | NOT APPROVED | use: CORRECT (adj); CORRECTLY (adv) |
| correspond (v) | NOT APPROVED | use: AGREE (v); SAME (adj); DIFFERENT (adj) |
| corresponding (adj) | NOT APPROVED | use: RELATED (adj) — "The corresponding caution light shall go off after 30 seconds." → "THE RELATED CAUTION LIGHT MUST GO OFF AFTER 30 SECONDS." |
| corrode (v) | NOT APPROVED | use: CORROSION (TN) — "This material corrodes unprotected surfaces." → "THIS MATERIAL CAUSES CORROSION OF SURFACES WITH NO PROTECTION." |
| corrosive (adj) | NOT APPROVED | use: CORROSION (TN) — "Hydraulic fluid is corrosive." → "HYDRAULIC FLUID CAN CAUSE CORROSION." |
| COUNT (v) | To add the number of objects or occurrences to get a total | forms: COUNTS, COUNTED, COUNTED |
| COUNTERCLOCKWISE (adv) | In the opposite direction to clockwise |  |
| couple (v) | NOT APPROVED | use: CONNECT (v); ATTACH (v) |
| cover (v) | NOT APPROVED | use: INCLUDE (v); HAVE (v); COVER (TN) |
| crack (v) | NOT APPROVED | use: OPEN (v); CRACK (TN) |
| create (v) | NOT APPROVED | use: MAKE (v); CAUSE (v) |
| critical (adj) | NOT APPROVED | use: VERY IMPORTANT; CAREFUL (adj) |
| cross (v) | NOT APPROVED | use: ACROSS (adv); CORRECTLY (adv) |
| curvature (n) | NOT APPROVED | use: BEND (n); CURVE (n); RADIUS (TN) |
| CURVE (n) | The shape of something which is bent but which has no angles |  |
| curve (v) | NOT APPROVED | use: MAKE A CURVE — "Curve the strip of metal." → "BEND THE STRIP OF METAL TO MAKE A CURVE." |
| CUT (v) | 1. To divide into parts 2. To remove with a sharp tool | forms: CUTS, CUT, CUT |
| CYCLE (n) | One complete sequence of operation |  |
| cycle (v) | NOT APPROVED | use: CYCLE (n) — "Cycle the actuator three times." → "OPERATE THE ACTUATOR THROUGH THREE CYCLES." |
| DAMAGE (n) | The result of an occurrence that causes deterioration of the condition of something |  |
| damage (v) | NOT APPROVED | use: DAMAGE (n) — "Disconnect the spring so as not to damage the rod." → "DISCONNECT THE SPRING TO PREVENT DAMAGE TO THE ROD." |
| DAMAGED (adj) | That has or can be affected by damage |  |
| damp (adj) | NOT APPROVED | use: MOIST (adj) — "Remove all dirt from the seat with a damp cloth." → "REMOVE ALL DIRT FROM THE SEAT WITH A MOIST CLOTH." |
| dampen (v) | NOT APPROVED | use: DECREASE (v); MAKE MOIST |
| danger (n) | NOT APPROVED | use: RISK (n) — DANGEROUS (adj) “danger” is a technical noun when it identifies a safety instruction. Refer to section 7. — "There is a danger of fire. Hydraulic fluid is a danger to your health." → "THERE IS A RISK OF FIRE. HYDRAULIC FLUID IS DANGEROUS FOR YOUR HEALTH." |
| DANGEROUS (adj) | That can cause injury, damage to health or can kill |  |
| dangerously (adv) | NOT APPROVED | use: DANGEROUS (adj) — "Do not open the cargo door if the wind-speed is dangerously high." → "DO NOT OPEN THE CARGO DOOR IN STRONG WINDS. STRONG WINDS ARE DANGEROUS." |
| DATA (n) | 1. Known facts 2. Numbers and symbols used by computers You can also use the singular. |  |
| DATE (n) | The time at which an event occurs |  |
| DEACTIVATE (v) | To make a system, function, or feature no longer ready for operation | For other meanings, use: STOP (v) |
| deadly (adj) | NOT APPROVED | use: KILL (v) — "High voltages are deadly." → "HIGH VOLTAGES CAN KILL YOU." |
| deaerate (v) | NOT APPROVED | use: BLEED (v); AIR (TN) |
| dearm (v) | NOT APPROVED | use: DISARM (v); REMOVE (v) |
| decay (v) | NOT APPROVED | use: DECREASE (v) — "When the engine speed decays to 500 rpm, stop the engine." → "WHEN THE ENGINE SPEED DECREASES TO 500 RPM, STOP THE ENGINE." |
| decelerate (v) | NOT APPROVED | use: DECREASE (v); SLOWER (adj) |
| decide (v) | NOT APPROVED | use: SELECT (v); DECISION (n) |
| DECISION (n) | The result after you think about a problem |  |
| decrease (n) | NOT APPROVED | use: DECREASE (v) — "There must be a decrease in pressure of more than 2 bar." → "THE PRESSURE MUST DECREASE BY MORE THAN 2 bar." |
| DECREASE (v) | To make or become smaller or lower | forms: DECREASES, DECREASED, DECREASED |
| decrement (n) | NOT APPROVED | use: INCREMENT (n) — "Turn the adjuster anticlockwise in decrements of 60 deg." → "TURN THE ADJUSTER COUNTERCLOCKWISE IN INCREMENTS OF 60 DEG." |
| DEDICATED (adj) | That is used only for one purpose |  |
| DE-ENERGIZE (v) | To remove electrical power from | forms: DE-ENERGIZES, DE-ENERGIZED, DE-ENERGIZED |
| DEEP (adj) | That has a specified depth | forms: (DEEPER, DEEPEST) |
| DEFECTIVE (adj) | Unserviceable for operation |  |
| define (v) | NOT APPROVED | use: CALCULATE (v); GIVE (v); SPECIFIED (adj) |
| DEFLATE (v) | To make or become smaller as a result of depressurization | forms: DEFLATES, DEFLATED, DEFLATED |
| deflect (v) | NOT APPROVED | use: MOVE (v) — "Bars deflect to the right." → "THE BARS MOVE TO THE RIGHT SIDE." |
| deflection (n) | NOT APPROVED | use: MOVEMENT (n); POSITION (n); TRAVEL (n) |
| deformed (adj) | NOT APPROVED | use: DAMAGED (adj); DEFORMATION (TN) |
| DEFUEL (v) | To remove fuel | forms: DEFUELS, DEFUELED, DEFUELED |
| defueling (n) | NOT APPROVED | use: DEFUEL (v) — "Only do the defueling in an open area that is well-ventilated." → "DEFUEL ONLY IN AN OPEN AREA THAT HAS A GOOD AIRFLOW." |
| degrease (v) | NOT APPROVED | use: GREASE (TN) — "Degrease the faying surface with solvent." → "REMOVE ALL GREASE FROM THE FAYING SURFACE WITH SOLVENT." |
| de-ice (v) | NOT APPROVED | use: ICE (TN) — "De-ice the window." → "REMOVE THE ICE FROM THE WINDOW." |
| delay (n) | NOT APPROVED | use: INTERVAL (n); IMMEDIATELY (adv) |
| delay (v) | NOT APPROVED | use: AFTER (prep) — "Use of the starter must be delayed for 20 minutes." → "ONLY USE THE STARTER AFTER A PERIOD OF 20 MINUTES." |
| delete (v) | NOT APPROVED | use: ERASE (v); REMOVE (v) |
| delicate (adj) | NOT APPROVED | use: EASILY DAMAGED — "Be careful with delicate parts." → "BE CAREFUL WITH EASILY DAMAGED PARTS." |
| deliver (v) | NOT APPROVED | use: SUPPLY (v) — "Set the rig so that it delivers a pressure of 800 kPa." → "SET THE RIG TO SUPPLY A PRESSURE OF 800 kPa." |
| delivery (n) | NOT APPROVED | use: SUPPLY (v) — "Hydraulic fluid delivery to the unit is ensured by a centrifugal pump." → "A CENTRIFUGAL PUMP SUPPLIES HYDRAULIC FLUID TO THE UNIT." |
| demand (v) | NOT APPROVED | use: NECESSARY (adj) — "This configuration demands a different test procedure." → "IN THIS CONFIGURATION, A DIFFERENT TEST PROCEDURE IS NECESSARY." |
| denote (v) | NOT APPROVED | use: SHOW (v) — "Figure 2 denotes that an alternative relay may be installed." → "FIGURE 2 SHOWS THAT YOU CAN INSTALL AN ALTERNATIVE RELAY." |
| dent (v) | NOT APPROVED | use: DENT (TN) — "Do not dent the bellows." → "DO NOT MAKE DENTS IN THE BELLOWS." |
| depend (v) | NOT APPROVED | use: IF (conj) — "Cable tension changes depending on the temperature." → "THE TENSION IN THE CABLES DECREASES IF THE TEMPERATURE INCREASES." |
| deplete (v) | NOT APPROVED | use: DECREASE (v) — "Do not deplete accumulators by operating the brakes." → "DO NOT OPERATE THE BRAKES TO DECREASE THE PRESSURE IN THE ACCUMULATORS." |
| DEPLOY (v) | To move or cause to move from a specified position of storage and into operation | forms: DEPLOYS, DEPLOYED, DEPLOYED |
| deposit (n) | NOT APPROVED | use: PARTICLE (n); CONTAMINATION (n) |
| depress (v) | NOT APPROVED | use: PUSH (v) — "Depress and release the button." → "PUSH THE BUTTON AND THEN RELEASE IT." |
| depressurize (v) | NOT APPROVED | use: PRESSURE (TN) — "Depressurize the hydraulic system." → "RELEASE THE PRESSURE FROM THE HYDRAULIC SYSTEM." |
| DEPTH (n) | The distance from the top down, from the surface down, from the front surface to the rear surface |  |
| describe (v) | NOT APPROVED | use: GIVE (v) — "This section describes the procedures for testing the system for leaks." → "THIS SECTION GIVES THE PROCEDURES FOR THE LEAK TEST OF THE SYSTEM." |
| deselect (v) | NOT APPROVED | use: CANCEL (v) — "Press the button to deselect the freeze mode." → "PUSH THE BUTTON TO CANCEL THE FREEZE MODE." |
| design (v) | NOT APPROVED | use: HAVE (v) — "The main landing gear doors are designed with steps for access to the landing gear bay." → "THE MAIN LANDING GEAR DOORS HAVE STEPS FOR ACCESS TO THE LANDING GEAR BAY." |
| desired (adj) | NOT APPROVED | use: NECESSARY (adj); CORRECT (adj) |
| destroy (v) | NOT APPROVED | use: BREAK (v) — "To prevent further use, destroy the container." → "BREAK THE CONTAINER TO MAKE SURE THAT YOU CANNOT USE IT AGAIN." |
| detach (v) | NOT APPROVED | use: DISCONNECT (v); DISENGAGE (v); REMOVE (v) |
| detail (n) | NOT APPROVED | use: INSTRUCTION (n) — "This procedure gives details on how to attach the pylon." → "THIS PROCEDURE GIVES THE INSTRUCTIONS TO ATTACH THE PYLON." |
| detail (v) | NOT APPROVED | use: GIVE (v); REFER (v); SPECIFIED (adj) |
| detect (v) | NOT APPROVED | use: FIND (v); SENSE (v) |
| DETERIORATION (n) | A worse condition |  |
| determine (v) | NOT APPROVED | use: FIND (v); GIVE (v); SELECT (v); CALCULATE (v) |
| detrimental (adj) | NOT APPROVED | use: DANGEROUS (adj); DAMAGE (n) |
| develop (v) | NOT APPROVED | use: START (v); CAUSE (v) |
| deviate (v) | NOT APPROVED | use: OBEY (v) — "Personnel must not deviate from this procedure." → "PERSONNEL MUST OBEY THIS PROCEDURE." |
| DEVICE (n) | Something used to do a task |  |
| devise (v) | NOT APPROVED | use: MAKE (v); FIND (v) |
| diagnose (v) | NOT APPROVED | use: FIND (v) — "Diagnose the cause of the malfunction." → "FIND THE CAUSE OF THE MALFUNCTION." |
| DIAGONALLY (adv) | In a diagonal direction |  |
| diametrically (adv) | NOT APPROVED | use: OPPOSITE (adj) — "Ensure the two diametrically opposed V-grooves are in line with the rails." → "MAKE SURE THAT THE TWO OPPOSITE V-GROOVES ALIGN WITH THE RAILS." |
| differ (v) | NOT APPROVED | use: DIFFERENT (adj) — "If the values differ, do the following test." → "IF THE VALUES ARE DIFFERENT, DO THIS TEST." |
| DIFFERENCE (n) | That which is different between two quantities, numbers, or functions |  |
| DIFFERENT (adj) | Not the same |  |
| DIFFERENTLY (adv) | In a different manner |  |
| differentiate (v) | NOT APPROVED | use: IDENTIFY (v) — "Letters are used to differentiate between the wire segments." → "LETTERS IDENTIFY THE WIRE SEGMENTS." |
| difficult (adj) | NOT APPROVED | use: NOT EASY; NOT EASILY |
| difficulty (n) | NOT APPROVED | use: NOT EASY; NOT EASILY |
| DIGITAL (adj) | Related to digits |  |
| DIGITALLY (adv) | Given by digits |  |
| dilute (v) | NOT APPROVED | use: MIX (v); ADD (v) |
| dim (v) | NOT APPROVED | use: DECREASE (v) — "Dim the light gradually." → "DECREASE THE LIGHT GRADUALLY." |
| DIM (adj) | Not bright | forms: (DIMMER, DIMMEST) |
| DIMENSION (n) | The result when something is measured in one direction |  |
| diminish (v) | NOT APPROVED | use: DECREASE (v) — "If the hydraulic pressure diminishes, close the valve." → "IF THE HYDRAULIC PRESSURE DECREASES, CLOSE THE VALVE." |
| DIMLY (adv) | Not bright |  |
| dip (v) | NOT APPROVED | use: MOMENTARILY (adv) — "Dip the element in solvent." → "PUT THE ELEMENT INTO THE SOLVENT MOMENTARILY." |
| direct (v) | NOT APPROVED | use: POINT (v) — "Direct the open end of the drain hose away from the structure." → "POINT THE OPEN END OF THE DRAIN HOSE AWAY FROM THE STRUCTURE." |
| DIRECTION (n) | The line on which something moves or is pointed |  |
| DIRECTLY (adv) | In a direct procedure or by direct effect |  |
| DIRTY (adj) | Not clean | forms: (DIRTIER, DIRTIEST) |
| disappear (v) | NOT APPROVED | use: VIEW (n) — "The horizontal bar disappears from the window." → "THE HORIZONTAL BAR GOES OUT OF VIEW." |
| DISARM (v) | 1. To remove armaments 2. To prevent automatic operation | forms: DISARMS, DISARMED, DISARMED |
| DISASSEMBLE (v) | To take an assembly apart | forms: DISASSEMBLES, DISASSEMBLED, DISASSEMBLED |
| DISCARD (v) | To not use again | forms: DISCARDS, DISCARDED, DISCARDED |
| discharge (v) | NOT APPROVED | use: RELEASE (v); GO (v) |
| DISCONNECT (v) | To separate something from the thing that it is connected to, or to become separated | forms: DISCONNECTS, DISCONNECTED, DISCONNECTED |
| discontinue (v) | NOT APPROVED | use: STOP (v) — "Discontinue the test procedure." → "STOP THE TEST PROCEDURE." |
| discover (v) | NOT APPROVED | use: FIND (v) — "If you discover corrosion during the inspection, remove it." → "IF YOU FIND CORROSION DURING THE INSPECTION, REMOVE IT." |
| discrepancy (n) | NOT APPROVED | use: DIFFERENCE (n) — "If the discrepancy is greater than 5 mm, check the adjustment." → "IF THERE IS A DIFFERENCE OF MORE THAN 5 mm, MAKE SURE THAT THE ADJUSTMENT IS CORRECT." |
| DISENGAGE (v) | To release or become released from something that engages | forms: DISENGAGES, DISENGAGED, DISENGAGED |
| disinfect (v) | NOT APPROVED | use: DISINFECTANT (TN) — "Disinfect the mask assemblies." → "USE DISINFECTANT TO CLEAN THE MASK ASSEMBLIES." |
| dismantle (v) | NOT APPROVED | use: DISASSEMBLE (v) — "Dismantle the brake unit in the workshop." → "DISASSEMBLE THE BRAKE UNIT IN THE WORKSHOP." |
| dispatch (v) | NOT APPROVED | use: SEND (v) — "Dispatch a report to the Inspection Department." → "SEND A REPORT TO THE INSPECTION DEPARTMENT." |
| disperse (v) | NOT APPROVED | use: REMOVE (v) — "Blow through the tubes to disperse the residual fluid." → "BLOW THROUGH THE TUBES TO REMOVE THE REMAINING FLUID." |
| displace (v) | NOT APPROVED | use: MOVE (v) — "Fluid is displaced by the piston." → "THE PISTON MOVES THE FLUID." |
| DISPLAY (n) | A visual indication |  |
| display (v) | NOT APPROVED | use: SHOW (v) — "The headings are displayed on the compass indicators." → "THE COMPASS INDICATORS SHOW THE HEADINGS." |
| dispose of (v) | NOT APPROVED | use: DISCARD (v) — "Dispose of the used oil according to the applicable environmental regulations." → "DISCARD THE USED OIL. REFER TO THE APPLICABLE ENVIRONMENTAL REGULATIONS." |
| disposition (n) | NOT APPROVED | use: LOCATION (n); POSITION (n) |
| disregard (v) | NOT APPROVED | use: IGNORE (v) — "Perform the generator drive test, but disregard steps 16 thru 20." → "DO THE GENERATOR DRIVE TEST, BUT IGNORE STEPS 16 THRU 20." |
| DISTANCE (n) | The dimension between two points or objects |  |
| distinct (adj) | NOT APPROVED | use: CLEAR (adj) — "Ensure the sound is distinct." → "MAKE SURE THAT THE SOUND IS CLEAR." |
| distinctly (adv) | NOT APPROVED | use: CLEARLY (adv) — "You must adjust the volume until you hear the sound distinctly." → "ADJUST THE VOLUME UNTIL YOU HEAR THE SOUND CLEARLY." |
| distort (v) | NOT APPROVED | use: TWIST (v) — "Do not distort the pipe when turning the connectors." → "WHEN YOU TURN THE CONNECTORS, DO NOT TWIST THE PIPE." |
| distribute (v) | NOT APPROVED | use: APPLY (v); SUPPLY (v) |
| distribution (n) | NOT APPROVED | use: SUPPLY (n) — "The fuel distribution is from the collector tanks." → "THE FUEL SUPPLY IS FROM THE COLLECTOR TANKS." |
| disturb (v) | NOT APPROVED | use: MOVE (v); CHANGE (v) |
| DIVIDE (v) | 1. To separate into parts or groups 2. To do mathematical division | forms: DIVIDES, DIVIDED, DIVIDED |
| DO (v) | 1. To complete a procedure, task, or step 2. As an auxiliary verb a. As part of a negative command or statement b. As part of a question | forms: DOES, DID, DONE |
| don (v) | NOT APPROVED | use: USE (v); PUT ON (v) |
| doubt (n) | NOT APPROVED | use: NOT SURE; THINK (v) |
| DOWN (adj) | In a position below |  |
| DOWN (adv) | To a position below |  |
| DOWN (prep) | To a position below |  |
| DOWNSTREAM (adj) | In the direction of the flow |  |
| DOWNSTREAM (adv) | In the direction of the flow |  |
| DOWNSTREAM OF (prep) | In the direction of the flow |  |
| downward (adv) | NOT APPROVED | use: DOWN (adv) — "Make sure that the air outlet is positioned downward." → "MAKE SURE THAT THE AIR OUTLET POINTS DOWN." |
| drag (v) | NOT APPROVED | use: PULL (v) — "Drag the wires through the conduit." → "PULL THE WIRES THROUGH THE CONDUIT." |
| DRAIN (v) | To remove liquid | forms: DRAINS, DRAINED, DRAINED |
| draw (v) | NOT APPROVED | use: MAKE (v); PULL (v) |
| dress (v) | NOT APPROVED | use: USE (v); PUT ON (v) |
| drift (v) | NOT APPROVED | use: MOVE (v); REMOVE (v) — (WITH A DRIFT [TN]) |
| DRINK (v) | To consume liquid | For safety instructions, use: SWALLOW (v); forms: DRINKS, DRANK, No other verb forms. |
| drive (v) | NOT APPROVED | use: MOVE (v); REMOVE (v); OPERATE (v) |
| droop (v) | NOT APPROVED | use: MOVE (v) — "If you do not install the rigging pin, the elevators will droop when there is no pressure in the system." → "IF YOU DO NOT INSTALL THE RIGGING PIN, THE ELEVATORS WILL MOVE DOWN WHEN THERE IS NO PRESSURE IN THE SYSTEM." |
| DROP (n) | A small quantity of liquid in a spherical shape |  |
| drop (v) | NOT APPROVED | use: FALL (v); DECREASE (v) |
| DRY (adj) | Without liquid or moisture | forms: (DRIER, DRIEST) |
| DRY (v) | To remove liquid or moisture, or to become dry | forms: DRIES, DRIED, DRIED |
| due to (prep) | NOT APPROVED | use: BECAUSE OF (prep); BECAUSE (conj) |
| dull (adj) | NOT APPROVED | use: DIM (adj); MATT (adj) |
| duration (n) | NOT APPROVED | use: DURING (prep) — "Do not make adjustments for the duration of this test." → "DO NOT MAKE ADJUSTMENTS DURING THIS TEST." |
| DURING (prep) | In or for a specified time |  |
| dust (v) | NOT APPROVED | use: APPLY (v) — "Dust the area with talcum powder." → "APPLY TALCUM POWDER TO THE AREA." |
| EACH (adj) | Every one of two or more objects or persons, seen together as a group but identified separately |  |
| EACH (pron) | Every one of two or more objects or persons, seen together as a group but identified separately |  |
| EACH OTHER (pron) | Each of two or more in reciprocal action or relation |  |
| early (adj) | NOT APPROVED | use: SHORT (adj) — "If the filters clog at an unusually early stage, send them to the laboratory for analysis of the contamination." → "IF THE FILTERS BECOME CLOGGED AFTER AN UNUSUALLY SHORT TIME, SEND THEM TO THE LABORATORY FOR ANALYSIS OF THE CONTAMINATION." |
| earth (n) | NOT APPROVED | use: GROUND (n) — "Make sure the electric supply goes to earth." → "MAKE SURE THAT THE ELECTRICAL SUPPLY GOES TO GROUND." |
| earth (v) | NOT APPROVED | use: GROUND (v) — "Make sure the fuel tanks are correctly earthed." → "MAKE SURE THAT THE FUEL TANKS ARE CORRECTLY GROUNDED." |
| ease (n) | NOT APPROVED | use: EASILY (adv); EASY (adj) |
| ease (v) | NOT APPROVED | use: CAREFULLY REMOVE; CAREFULLY MOVE |
| EASILY (adv) | Without difficulty |  |
| EASY (adj) | Without difficulty | forms: (EASIER, EASIEST) |
| EAT (v) | To consume food | For safety instructions, use: SWALLOW (v); forms: EATS, ATE No other verb forms. |
| EDGE (n) | A line that is the intersection of two surfaces of a solid object |  |
| EFFECT (n) | The result of a cause |  |
| effect (v) | NOT APPROVED | use: DO (v) — "Effect the tightening procedure." → "DO THE TIGHTENING PROCEDURE." |
| effective (adj) | NOT APPROVED | use: GOOD (adj) — "This material provides effective protection from corrosion." → "THIS MATERIAL GIVES GOOD PROTECTION FROM CORROSION." |
| efficacious (adj) | NOT APPROVED | use: GOOD (adj) — "This is an efficacious way to remove paint." → "THIS IS A GOOD PROCEDURE TO REMOVE PAINT." |
| efficient (adj) | NOT APPROVED | use: SATISFACTORY (adj) — "The Transmission Control Protocol is not efficient for the transmission of interactive traffic." → "THE TRANSMISSION CONTROL PROTOCOL IS NOT SATISFACTORY FOR THE TRANSMISSION OF INTERACTIVE TRAFFIC." |
| efficiently (adv) | NOT APPROVED | use: SATISFACTORILY (adv) — "Make sure the unit operates efficiently." → "MAKE SURE THAT THE UNIT OPERATES SATISFACTORILY." |
| efflux (n) | NOT APPROVED | use: EXHAUST (n) — "Ensure that there are safety barriers around the engine efflux area." → "MAKE SURE THAT THERE ARE SAFETY BARRIERS AROUND THE ENGINE EXHAUST AREA." |
| effort (n) | NOT APPROVED | use: FORCE (TN); TRY (v) |
| either (adj) | NOT APPROVED | ONE (TN) OF THE TWO (TN) — "If there is mercury spillage in either compartment, clean the area immediately." → "IF THERE IS MERCURY CONTAMINATION IN ONE OF THE TWO COMPARTMENTS, CLEAN THE AREA IMMEDIATELY." |
| either (conj) | NOT APPROVED | use: OR (conj) — "You can use either a red pen or a green pen." → "YOU CAN USE A RED PEN OR A GREEN PEN." |
| either (pron) | NOT APPROVED | use: OTHER — ONE (TN) OR THE — "There are two solenoids. You can supply electrical power to either." → "THERE ARE TWO SOLENOIDS. YOU CAN SUPPLY ELECTRICAL POWER TO ONE OR THE OTHER." |
| EJECT (v) | To move or to cause a person or item to move from an aircraft or equipment with force | forms: EJECTS, EJECTED, EJECTED |
| ejection (n) | NOT APPROVED | use: EJECT (v) — "Push the applicable button for disk drive ejection." → "PUSH THE APPLICABLE BUTTON TO EJECT THE DISK DRIVE." |
| elapse (v) | NOT APPROVED | use: TIME (n); AFTER (prep); INTERVAL (n) |
| ELECTRIC (adj) | Operated by electricity |  |
| ELECTRICAL (adj) | Related to electricity |  |
| ELECTRICALLY (adv) | Related to or operated by electricity |  |
| ELECTROMAGNETIC (adj) | Related to electromagnetism |  |
| ELECTROMAGNETICALLY (adv) | Related to electromagnetism |  |
| ELECTRONIC (adj) | Related to or operated by electronics |  |
| ELECTRONICALLY (adv) | Related to or operated by electronics |  |
| eliminate (v) | NOT APPROVED | use: REMOVE (v); STOP (v); PREVENT (v) |
| EMERGENCY (n) | A condition that occurs suddenly and is dangerous |  |
| emit (v) | NOT APPROVED | use: FROM (prep) — "The vapors that this material emits are dangerous to the skin." → "THE VAPORS FROM THIS MATERIAL ARE DANGEROUS TO THE SKIN." |
| employ (v) | NOT APPROVED | use: USE (v); HAVE (v) |
| EMPTY (adj) | Without contents |  |
| empty (v) | NOT APPROVED | use: REMOVE (v) — "Empty the fuel tanks." → "REMOVE ALL FUEL FROM THE FUEL TANKS." |
| enable (v) | NOT APPROVED | use: LET (v) — "The disassembly fixture enables you to disassemble the module." → "THE DISASSEMBLY FIXTURE LETS YOU DISASSEMBLE THE MODULE." |
| encircle (v) | NOT APPROVED | use: AROUND (prep) — "Encircle each screw hole with sealant." → "PUT SEALANT AROUND EACH SCREW HOLE." |
| enclosed (adj) | NOT APPROVED | use: CLOSED (adj) — "The work area must be well-ventilated if solvent is used in an enclosed space." → "IF YOU USE SOLVENT IN A CLOSED SPACE, MAKE SURE THAT THERE IS GOOD AIRFLOW IN THE WORK AREA." |
| encounter (v) | NOT APPROVED | use: BE (v); FIND (v) |
| END (n) | Where time, distance, or sequence are completed |  |
| end (v) | NOT APPROVED | use: STOP (v); COMPLETE (v) |
| ENERGIZE (v) | To supply electrical power to | forms: ENERGIZES, ENERGIZED, ENERGIZED |
| enforce (v) | NOT APPROVED | use: OBEY (v) — "Safety precautions must be enforced." → "ALL PERSONNEL MUST OBEY THE SAFETY PRECAUTIONS." |
| ENGAGE (v) | To correctly align and come together | forms: ENGAGES, ENGAGED, ENGAGED |
| engagement (n) | NOT APPROVED | use: ENGAGE (v) — "Make sure there is full engagement of the splines." → "MAKE SURE THAT THE SPLINES ENGAGE FULLY." |
| enlarge (v) | NOT APPROVED | use: INCREASE (v); LARGE (adj) |
| enough (adj) | NOT APPROVED | use: SUFFICIENT (adj) — "Make sure that there is enough pressure in the accumulator." → "MAKE SURE THAT THERE IS SUFFICIENT PRESSURE IN THE ACCUMULATOR." |
| ensue (v) | NOT APPROVED | use: CAUSE (v) — "Damage will ensue from incorrect installation." → "INCORRECT INSTALLATION WILL CAUSE DAMAGE." |
| ensure (v) | NOT APPROVED | use: MAKE SURE (v) — "Ensure that the correct seals are installed." → "MAKE SURE THAT THE CORRECT SEALS ARE INSTALLED." |
| enter (v) | NOT APPROVED | use: GO INTO; RECORD (v); ENTRY (n) |
| entire (adj) | NOT APPROVED | use: FULL (adj); ALL (adj) |
| entirely (adv) | NOT APPROVED | use: FULLY (adv) — "The system is entirely automatic." → "THE SYSTEM IS FULLY AUTOMATIC." |
| ENTRANCE (n) | An opening to go into a space |  |
| ENTRY (n) | A record of an occurrence |  |
| EQUAL (adj) | The same dimension, quality, quantity, or number |  |
| equal (v) | NOT APPROVED | use: SAME (adj); EQUAL (adj) |
| EQUALLY (adv) | The same dimension, quality, quantity, or number |  |
| equip (v) | NOT APPROVED | use: INSTALL (v) — "Equip each HP manifold with shutoff valves." → "INSTALL THE SHUTOFF VALVES ON EACH HP MANIFOLD." |
| EQUIPMENT (n) | The objects or tools used for operation and maintenance |  |
| equipped (adj) | NOT APPROVED | use: HAVE (v) — "Be careful when handling jet pipes or exhaust cones equipped with insulating blankets." → "BE CAREFUL WHEN YOU MOVE JET PIPES OR EXHAUST CONES THAT HAVE INSULATING BLANKETS." |
| EQUIVALENT (adj) | Has the same properties, functions, or values |  |
| EQUIVALENT (n) | Something that has the same properties, functions, or values |  |
| ERASE (v) | To remove data from a medium | forms: ERASES, ERASED, ERASED |
| erect (v) | NOT APPROVED | use: ASSEMBLE (v); BECOME STABLE |
| erratic (adj) | NOT APPROVED | use: IRREGULAR (adj) — "The compass is erratic." → "THE OPERATION OF THE COMPASS IS IRREGULAR." |
| ERROR (n) | The difference from that which is correct or accurate |  |
| escape (v) | NOT APPROVED | use: DEFLATE (v); RELEASE (v) |
| establish (v) | NOT APPROVED | use: MAKE SURE (v) — "In the following step, establish the correct functioning of the fuel pump." → "IN THE STEP THAT FOLLOWS, MAKE SURE THAT THE FUEL PUMP OPERATES CORRECTLY." |
| ESTIMATE (n) | A calculated, approximate result |  |
| estimate (v) | NOT APPROVED | use: ESTIMATE (n) — "Estimate the amount of cleaning fluid that is necessary." → "MAKE AN ESTIMATE OF THE QUANTITY OF CLEANING FLUID THAT IS NECESSARY." |
| evaluate (v) | NOT APPROVED | use: EXAMINE (v); ANALYSIS (TN) |
| evaluation (n) | NOT APPROVED | use: EXAMINE (v); ANALYSIS (TN) |
| evaporate (v) | NOT APPROVED | use: DRY (v) — "Allow the solvent to evaporate from the compound." → "LET THE COMPOUND DRY." |
| even (adj) | NOT APPROVED | use: SMOOTH (adj); SAME (adj); FLAT (adj); FLUSH (adj); LEVEL (adj) |
| evenly (adv) | NOT APPROVED | use: GRADUALLY (adv); EQUALLY (adv) |
| event (n) | NOT APPROVED | use: IF (conj) — "In the event of a sudden dropping of pressure, close the valve." → "IF THE PRESSURE DECREASES SUDDENLY, CLOSE THE VALVE." |
| eventually (adv) | NOT APPROVED | use: SOME TIME — "If the cable chafes, it will eventually break." → "IF THE CABLE RUBS, IT WILL BREAK AFTER SOME TIME." |
| every (adj) | NOT APPROVED | use: ALL (adj); EACH (adj); INTERVAL (n) |
| evidence (n) | NOT APPROVED | use: INDICATION (n); SIGN (n); SHOW (v) |
| evidence (v) | NOT APPROVED | use: SHOW (v); FIND (v) |
| evident (adj) | NOT APPROVED | use: FIND (v) — "If no damage is evident, continue the inspection." → "IF YOU DO NOT FIND DAMAGE, CONTINUE THE INSPECTION." |
| exact (adj) | NOT APPROVED | use: ACCURATE (adj); CORRECT (adj) |
| exactly (adv) | NOT APPROVED | use: ACCURATELY (adv); FULLY (adv); CORRECT (adj) |
| examination (n) | NOT APPROVED | use: EXAMINE (v); FIND (v) |
| EXAMINE (v) | To look carefully at | forms: EXAMINES, EXAMINED, EXAMINED |
| EXAMPLE (n) | Something from a group which has the same qualities as the group |  |
| exceed (v) | NOT APPROVED | use: MORE THAN — "Ensure that the indication does not exceed 400 knots." → "MAKE SURE THAT THE INDICATION IS NOT MORE THAN 400 KNOTS." |
| except (prep) | NOT APPROVED | To replace this word, use a different construction. Be accurate. — "Keep all parts except those that are broken. Remove all screws except the one on the left side of the flange." → "KEEP ALL THE PARTS THAT ARE SERVICEABLE AND DISCARD THOSE THAT ARE BROKEN. REMOVE ALL SCREWS, BUT NOT THE ONE ON THE LEFT SIDE OF THE FLANGE." |
| exception (n) | NOT APPROVED | To replace this word, use a different construction. Be accurate. — "Keep all parts with the exception of those that are broken. Remove all screws with the exception of the one on the left side of the flange." → "KEEP ALL THE PARTS THAT ARE SERVICEABLE AND DISCARD THOSE THAT ARE BROKEN. REMOVE ALL SCREWS, BUT NOT THE ONE ON THE LEFT SIDE OF THE FLANGE." |
| exceptional (adj) | NOT APPROVED | use: UNUSUAL (adj) — "If exceptional force is needed to open the unit, examine the control linkage." → "IF IT IS NECESSARY TO APPLY UNUSUAL FORCE TO OPEN THE UNIT, EXAMINE THE CONTROL LINKAGE." |
| exceptionally (adv) | NOT APPROVED | use: UNUSUALLY (adv) — "If the tire pressure is exceptionally high, open the valve." → "IF THE TIRE PRESSURE IS UNUSUALLY HIGH, OPEN THE VALVE." |
| excess (adj) | NOT APPROVED | use: TOO MUCH; MORE THAN; UNWANTED (adj); NOT NECESSARY |
| excess (n) | NOT APPROVED | use: TOO MUCH; MORE THAN |
| excessive (adj) | NOT APPROVED | use: TOO MUCH; MORE THAN |
| excessively (adv) | NOT APPROVED | use: TOO MUCH; MORE THAN |
| exchange (v) | NOT APPROVED | use: INTERCHANGE (v); REPLACE (v) |
| exclude (v) | NOT APPROVED | use: NOT INCLUDE; NOT USE |
| excluding (prep) | NOT APPROVED | use: WITHOUT (prep) — "The weight of the unit, excluding the motor, is 10 kg." → "THE WEIGHT OF THE UNIT, WITHOUT THE MOTOR, IS 10 kg." |
| execute (v) | NOT APPROVED | use: DO (v) — "Execute the following operations." → "DO THESE STEPS." |
| exempt (adj) | NOT APPROVED | use: NO (adj); NOT SHOW |
| exercise (v) | NOT APPROVED | use: MAKE SURE (v); CAREFUL (adj) |
| exert (v) | NOT APPROVED | use: APPLY (v); PUT (v) |
| exhale (v) | NOT APPROVED | use: BREATHE (v) — "Exhale into the oxygen mask." → "BREATHE INTO THE OXYGEN MASK." |
| EXHAUST (n) | The gas from an engine |  |
| exhaust (v) | NOT APPROVED | use: REMOVE (v); DECREASE (v); RELEASE (v) |
| exhaustive (adj) | NOT APPROVED | use: ALL (adj); FULL (adj) |
| exist (v) | NOT APPROVED | use: BE (v) — "Two different procedures exist for this repair." → "THERE ARE TWO DIFFERENT PROCEDURES FOR THIS REPAIR." |
| EXIT (n) | An opening to go out of a space |  |
| EXPAND (v) | To increase in dimension, volume, or time | forms: EXPANDS, EXPANDED, EXPANDED |
| expect (v) | NOT APPROVED | use: POSSIBLE (adj) — "If temperature is expected to drop to -20 degrees C, remove the batteries." → "IF IT IS POSSIBLE THAT THE TEMPERATURE WILL DECREASE TO -20 DEGREES C, REMOVE THE BATTERIES." |
| expel (v) | NOT APPROVED | use: REMOVE (v); BLEED (v); RELEASE (v) |
| EXPIRED (adj) | More than the permitted life |  |
| explain (v) | NOT APPROVED | use: TELL (v) — "The technician will explain the sensor calibration procedure to the operator." → "THE TECHNICIAN WILL TELL THE OPERATOR THE PROCEDURE FOR SENSOR CALIBRATION." |
| EXPLOSION (n) | The effect when an explosive material quickly releases its energy |  |
| EXPLOSIVE (adj) | That can cause an explosion |  |
| expose (v) | NOT APPROVED | use: GET (v) — "Remove cover assembly to expose lamp assembly." → "REMOVE THE COVER ASSEMBLY TO GET ACCESS TO THE LAMP ASSEMBLY." |
| EXTEND (v) | To increase, or cause something to increase, in dimension or range | forms: EXTENDS, EXTENDED, EXTENDED |
| EXTENSION (n) | 1. The action when something extends 2. The result when something extends |  |
| extent (n) | NOT APPROVED | use: DEPTH (n); LENGTH (n); WIDTH (n) |
| exterior (n) | NOT APPROVED | use: EXTERNAL (adj) — "Examine the exterior of the container." → "EXAMINE THE EXTERNAL SURFACE OF THE CONTAINER." |
| EXTERNAL (adj) | Of, or on, the outer side |  |
| EXTERNALLY (adv) | Of, or on, the outer side |  |
| EXTINGUISH (v) | To stop burning | For lights or lamps, use: GO OFF BE OFF; forms: EXTINGUISHES, EXTINGUISHED, EXTINGUISHED |
| extra (adj) | NOT APPROVED | use: MORE (adj) — "This material provides extra protection." → "THIS MATERIAL GIVES MORE PROTECTION." |
| extract (v) | NOT APPROVED | use: REMOVE (v) — "Extract the bolt." → "REMOVE THE BOLT." |
| extreme (adj) | NOT APPROVED | use: VERY HIGH (adj); VERY BAD (adj); VERY COLD (adj); VERY HOT (adj) |
| extremely (adv) | NOT APPROVED | use: VERY (adv) — "It is extremely important to observe the safety precautions." → "IT IS VERY IMPORTANT TO OBEY THE SAFETY PRECAUTIONS." |
| exude (v) | NOT APPROVED | use: OUT OF (prep) — "Make sure grease exudes from the joint." → "MAKE SURE THAT GREASE COMES OUT OF THE JOINT." |
| fabricate (v) | NOT APPROVED | use: MAKE (v) — "Use copper to fabricate the chill block." → "USE COPPER TO MAKE THE CHILL BLOCK." |
| FACE (n) | The front surface of an object This word is a technical noun when it refers to a part of the body. |  |
| face (v) | NOT APPROVED | use: POINT (v); TURN (v) |
| facilitate (v) | NOT APPROVED | use: HELP (v) — MAKE … EASIER — "Mark the component with a code that will facilitate its correct reinstallation. This facilitates fault isolation." → "IDENTIFY THE COMPONENT WITH A CODE TO HELP YOU TO CORRECTLY INSTALL IT AGAIN. THIS MAKES FAULT ISOLATION EASIER." |
| facility (n) | NOT APPROVED | Be accurate. Use the name of the facility as a technical noun. — "You need a special facility to weigh the aircraft." → "WEIGH THE AIRCRAFT ON A WEIGHBRIDGE." |
| FACT (n) | Something that occurred or is correct |  |
| factor (n) | NOT APPROVED | use: CAUSE (n) — "Corrosion can be caused by several factors." → "THERE CAN BE MANY CAUSES FOR CORROSION." |
| fail (v) | NOT APPROVED | use: FAILURE (TN); UNSATISFACTORY (adj) — IF … NOT |
| failed (adj) | NOT APPROVED | use: DEFECTIVE (adj); UNSERVICEABLE (adj) |
| failure (n) | NOT APPROVED | IF … NOT This word when it means a performance error or loss of serviceability is a technical noun. — "Failure to comply with these instructions, will result in a risk of injury." → "IF YOU DO NOT OBEY THESE INSTRUCTIONS, THERE IS A RISK OF INJURY. CONTAMINATION CAN CAUSE A FAILURE OF THE PUMP." |
| faint (adj) | NOT APPROVED | use: DIM (adj); INTENSITY (n); BRIGHT (adj). — Refer also to |
| fall (n) | NOT APPROVED | use: DECREASE (v) — "When there is a fall in pressure, the indicator shows a leak." → "WHEN THE PRESSURE DECREASES, THE INDICATOR SHOWS THAT THERE IS A LEAK." |
| FALL (v) | To move down by the force of gravity | forms: FALLS, FELL, FALLEN |
| false (adj) | NOT APPROVED | use: INCORRECT (adj) — "Make sure there are no false indications on the instruments." → "MAKE SURE THAT THERE ARE NO INCORRECT INDICATIONS ON THE INSTRUMENTS." |
| falter (v) | NOT APPROVED | use: SMOOTHLY (adv); CONSTANT (adj) |
| familiar (adj) | NOT APPROVED | use: KNOW (v) — "All personnel must be thoroughly familiar with the safety precautions." → "ALL PERSONNEL MUST FULLY KNOW THE SAFETY PRECAUTIONS." |
| FAR (adj) | At or to a relatively large distance | forms: (FARTHER, FARTHEST) |
| fashion (n) | NOT APPROVED | use: PROCEDURE (n) — "Carry out the task in this fashion." → "USE THIS PROCEDURE TO DO THE TASK." |
| FAST (adj) | At high speed | forms: (FASTER, FASTEST) |
| fast (adv) | NOT APPROVED | use: QUICKLY (adv) — "Do not let the cabin altitude change too fast." → "DO NOT LET THE CABIN ALTITUDE CHANGE TOO QUICKLY." |
| fasten (v) | NOT APPROVED | use: ATTACH (v); CONNECT (v) |
| fatal (adj) | NOT APPROVED | use: KILL (v) — "High voltage in the electronic system can be fatal." → "HIGH VOLTAGE IN THE ELECTRONIC SYSTEM CAN KILL YOU." |
| faulty (adj) | NOT APPROVED | use: DEFECTIVE (adj); INCORRECT (adj); UNSERVICEABLE (adj); UNSATISFACTORY (adj) |
| fear (v) | NOT APPROVED | use: THINK (v); MAKE SURE (v) |
| feasible (adj) | NOT APPROVED | use: POSSIBLE (adj) — CAN (CANNOT) (v) — "If it is not feasible to use the automatic control, do the manual procedure. If it is not feasible to remove the bolt, you must cut it." → "IF IT IS NOT POSSIBLE TO USE THE AUTOMATIC CONTROL, DO THE PROCEDURE MANUALLY. IF YOU CANNOT REMOVE THE BOLT, CUT IT." |
| FEATHER (v) | To put a propeller to a position of minimum drag | forms: FEATHERS, FEATHERED, FEATHERED |
| feature (v) | NOT APPROVED | use: HAVE (v) — "These nuts feature a flat flange." → "THESE NUTS HAVE A FLAT FLANGE." |
| feed (v) | NOT APPROVED | use: PUT (v); SUPPLY (v) |
| FEEL (v) | To touch to find | forms: FEELS, FELT, FELT |
| few (adj) | NOT APPROVED | use: SMALL NUMBER — If it is possible, give an accurate number. — "This procedure is only for repairs that include very few rivets." → "THIS PROCEDURE IS ONLY FOR REPAIRS THAT INCLUDE A VERY SMALL NUMBER OF RIVETS." |
| few (a few) (adj) | NOT APPROVED | use: SOME (adj) — If this alternative is not sufficient, give the range, number, or quantity. — "Let the engine run for a few minutes. After a few seconds, the light comes on again." → "LET THE ENGINE OPERATE FOR SOME MINUTES. AFTER APPROXIMATELY 5 SECONDS, THE LIGHT COMES ON AGAIN." |
| file (v) | NOT APPROVED | use: REMOVE (v) — (WITH A FILE (TN) — "Take care not to file too deeply." → "DO NOT REMOVE TOO MUCH MATERIAL WITH THE FILE." |
| filing (n) | NOT APPROVED | use: PARTICLE (n) — "Remove all the metal filings." → "REMOVE ALL THE METAL PARTICLES." |
| FILL (v) | To put into a container or a space to the maximum level or, if specified, to a given level, pressure, or quantity | forms: FILLS, FILLED, FILLED |
| film (n) | NOT APPROVED | use: LAYER (n) — "Spread a film of compound on the surface of the disc." → "APPLY A LAYER OF COMPOUND ON THE SURFACE OF THE DISC." |
| filter (v) | NOT APPROVED | use: FILTER (TN) — "Filter the oil." → "PUT THE OIL THROUGH A FILTER." |
| FILTERED (adj) | That has gone through a filter |  |
| final (adj) | NOT APPROVED | use: LAST (adj) — "The final action will open the valve." → "THE LAST STEP WILL OPEN THE VALVE." |
| FIND (v) | To discover, to examine something so that you know | forms: FINDS, FOUND, FOUND |
| finding (n) | NOT APPROVED | use: RESULT (n) — "Report the findings of the analysis to the quality department." → "TELL THE QUALITY DEPARTMENT ABOUT THE RESULTS OF THE ANALYSIS." |
| fine (adj) | NOT APPROVED | use: SMALL (adj) — "Only particles finer than 5 microns can go through the filter." → "ONLY PARTICLES SMALLER THAN 5 µm CAN GO THROUGH THE FILTER." |
| finger-tighten (v) | NOT APPROVED | use: YOUR FINGERS — TIGHTEN … WITH — "Finger-tighten the nut." → "TIGHTEN THE NUT WITH YOUR FINGERS." |
| FINISH (n) | The result of a finishing procedure |  |
| finish (v) | NOT APPROVED | use: COMPLETE (v) — "Finish the test." → "COMPLETE THE TEST." |
| FIRE (n) | The light and/or heat from a material when it burns |  |
| FIRE (v) | To ignite, or to operate items that contain an explosive material | forms: FIRES, FIRED, FIRED |
| firmly (adv) | NOT APPROVED | use: TIGHTLY (adv) — "Hold the cylinder firmly." → "HOLD THE CYLINDER TIGHTLY." |
| FIRST (adv) | Before other persons or things |  |
| FIT (n) | The relation between two related parts, a limit of tolerance |  |
| fit (v) | NOT APPROVED | use: INSTALL (v); ATTACH (v); CORRECT (adj) |
| fix (v) | NOT APPROVED | use: ATTACH (v); SET (v); REPAIR (v); INSTALL (v) |
| FLAME (n) | Burning gas |  |
| FLAMMABLE (adj) | That burns easily |  |
| FLANGE (n) | An end surface at an angle |  |
| FLASH (v) | To come on and go off frequently | forms: FLASHES, FLASHED, FLASHED |
| FLAT (adj) | That has a continuous surface in the same plane | forms: (FLATTER, FLATTEST) |
| flatness (n) | NOT APPROVED | use: FLAT (adj) — "A correct bond depends on the surface flatness." → "THE SURFACE MUST BE FLAT TO GET A CORRECT BOND." |
| flatten (v) | NOT APPROVED | use: FLAT (adj) — "Make sure that you do not flatten the tubes." → "MAKE SURE THAT YOU DO NOT CAUSE THE TUBES TO BECOME FLAT." |
| flaw (n) | NOT APPROVED | use: DAMAGE (n); DEFECTIVE (adj) — If it is possible, be accurate. |
| flex (v) | NOT APPROVED | use: BEND (v) — "The wing can flex up and down during flight." → "THE WING CAN BEND UP AND DOWN DURING FLIGHT." |
| FLEXIBLE (adj) | That can easily bend again and again |  |
| FLIGHT (n) | The time an aircraft is in the air |  |
| flood (v) | NOT APPROVED | use: USE TOO MUCH — "Do not flood the area with solvent." → "DO NOT USE TOO MUCH SOLVENT ON THE AREA." |
| FLOW (n) | A continuous movement of fluid |  |
| FLOW (v) | To move as a fluid moves | forms: FLOWS, FLOWED, FLOWED |
| fluctuate (v) | NOT APPROVED | use: CONSTANT (adj) — "Make sure that the pressure does not fluctuate." → "MAKE SURE THAT THE PRESSURE STAYS CONSTANT." |
| FLUID (n) | Liquid or gas |  |
| FLUSH (adj) | Of a surface that is level or continuous with another surface |  |
| FLUSH (v) | To remove something or to operate with a flow of liquid | forms: FLUSHES, FLUSHED, FLUSHED |
| focus (v) | NOT APPROVED | use: FOCUS (TN) — "Focus the optical fixture." → "PUT THE OPTICAL FIXTURE INTO FOCUS." |
| fold (n) | NOT APPROVED | use: FOLD (v) — "Make a fold in the material." → "FOLD THE MATERIAL." |
| FOLD (v) | To double over or to cause to double over on itself | forms: FOLDS, FOLDED, FOLDED |
| FOLLOW (v) | To come after, to go after | For other meanings, use: OBEY (v); forms: FOLLOWS, FOLLOWED, FOLLOWED |
| following (adj) | NOT APPROVED | use: THESE (adj); FOLLOW (v) |
| FOR (prep) | Function word that shows purpose, intent, time, result, or the object of an action |  |
| forbidden (adj) | NOT APPROVED | use: DO NOT; NOT PERMITTED |
| force (v) | NOT APPROVED | use: PUSH (v); FORCE (TN) |
| forecast (v) | NOT APPROVED | use: POSSIBLE (adj) — "If unfavorable weather conditions are forecast, moor the vessel securely." → "IF BAD WEATHER IS POSSIBLE, MOOR THE VESSEL SAFELY." |
| foreign (adj) | NOT APPROVED | use: UNWANTED (adj) — "This cover will prevent dirt, particles, or other foreign material from entering the system." → "THIS COVER WILL KEEP DIRT, PARTICLES, OR OTHER UNWANTED MATERIAL OUT OF THE SYSTEM." |
| foremost (adj) | NOT APPROVED | use: FRONT (n) — "The foremost half clamp is not removable." → "YOU CANNOT REMOVE THE HALF CLAMP THAT IS NEAREST TO THE FRONT." |
| form (n) | NOT APPROVED | use: SHAPE (n) — "The seal is in the form of an ellipse." → "THE SEAL HAS THE SHAPE OF AN ELLIPSE." |
| form (v) | NOT APPROVED | use: BE (v) — "If contamination has formed in the fuel tanks, remove it immediately." → "IF THERE IS CONTAMINATION IN THE FUEL TANKS, REMOVE IT IMMEDIATELY." |
| fortify (v) | NOT APPROVED | use: STRONG (adj) — "Carbon-fiber struts fortify the floor structure." → "CARBON-FIBER STRUTS MAKE THE FLOOR STRUCTURE STRONGER." |
| FORWARD (adj) | Nearer to the front |  |
| FORWARD (adv) | In the direction of the front |  |
| FORWARD OF (prep) | At a position nearer to the front |  |
| foul (v) | NOT APPROVED | use: CATCH (v); HIT (v); TOUCH (v); CLEARANCE (n) |
| fouled (adj) | NOT APPROVED | use: DIRTY (adj); CLOGGED (adj); CATCH (v) |
| fragile (adj) | NOT APPROVED | use: EASILY DAMAGED — "The water quantity transmitter is fragile." → "THE WATER QUANTITY TRANSMITTER IS EASILY DAMAGED." |
| FREE (adj) | That can move easily | Do not use compound adjectives with free, for example, lintfree, dustfree, unless they are technical nouns. |
| free from (adj) | NOT APPROVED | use: NO (adj) — "Make sure that the surface is free from dust." → "MAKE SURE THAT THERE IS NO DUST ON THE SURFACE." |
| free (v) | NOT APPROVED | use: RELEASE (v) — "Remove the sleeve to free the sliding tube." → "REMOVE THE SLEEVE TO RELEASE THE SLIDING TUBE." |
| FREELY (adv) | That can move easily |  |
| FREEZE (v) | To go or cause to go to a temperature below the freezing point of a liquid (usually of water) | forms: FREEZES, FROZE, FROZEN |
| FREQUENT (adj) | That occurs or is found often at short intervals |  |
| FREQUENTLY (adv) | At frequent or short intervals |  |
| fresh (adj) | NOT APPROVED | use: CLEAN (adj); NEW (adj) |
| FROM (prep) | Function word that shows a point of departure for movement, time, distance, action, or separation |  |
| FRONT (adj) | Nearer to the person that looks or a reference point Refer also to IN FRONT OF. |  |
| FRONT (n) | The front part or the front surface |  |
| fuel (v) | NOT APPROVED | use: REFUEL (v) — "Fuel the vehicle." → "REFUEL THE VEHICLE." |
| fulfill (v) | NOT APPROVED | use: OBEY (v) — "Fulfill the instructions in the test procedure. This procedure fulfills all the requirements of Service Bulletin No. 97." → "OBEY THE INSTRUCTIONS IN THE TEST PROCEDURE. THIS PROCEDURE OBEYS ALL THE REQUIREMENTS OF SERVICE BULLETIN No. 97." |
| FULL (adj) | At or related to maximum travel, length, quantity, or detail | forms: (FULLER, FULLEST) |
| FULLY (adv) | At or related to maximum travel, length, quantity, or detail |  |
| FUNCTION (n) | Action or activity that a person or thing does |  |
| function (v) | NOT APPROVED | use: OPERATE (v); MOVE (v) |
| fundamental (adj) | NOT APPROVED | use: IMPORTANT (adj) — "Cleanliness of all parts is fundamental in this procedure." → "DURING THIS PROCEDURE, IT IS IMPORTANT TO KEEP ALL PARTS CLEAN." |
| further (adj) | NOT APPROVED | use: MORE (adj) — "If you do not get the correct dimension, add further gaskets." → "IF YOU DO NOT GET THE CORRECT DIMENSION, ADD MORE GASKETS." |
| further (adv) | NOT APPROVED | use: MORE (adv) — "Cable tension can be further reduced if necessary by means of the turnbuckle." → "IF IT IS NECESSARY TO DECREASE THE CABLE TENSION MORE, USE THE TURNBUCKLE." |
| gain (n) | NOT APPROVED | use: INCREASE (v) — "The system’s efficiency showed a gain after the last modification." → "AFTER THE LAST MODIFICATION, THE SYSTEM’S EFFICIENCY INCREASED." |
| gain (v) | NOT APPROVED | use: GET (v) — "Gain access to the connectors at the back of the instrument." → "GET ACCESS TO THE CONNECTORS AT THE REAR OF THE INSTRUMENT." |
| gall (v) | NOT APPROVED | use: GALLING (TN) — "The surface must not be scratched or galled." → "THERE MUST BE NO SCRATCHES OR GALLING ON THE SURFACE." |
| gap (n) | NOT APPROVED | use: CLEARANCE (n); DISTANCE (n); SPACE (n) |
| garbled (adj) | NOT APPROVED | use: CLEAR (adj); CLEARLY (adv) |
| garner (v) | NOT APPROVED | use: COLLECT (v) — "These computers garner data from the VHF system. The BITE function garners the failures and sends the failure message to the Central Maintenance Computer." → "THESE COMPUTERS COLLECT DATA FROM THE VHF SYSTEM. THE BITE FUNCTION COLLECTS THE FAILURES AND SENDS THE FAILURE MESSAGE TO THE CENTRAL MAINTENANCE COMPUTER." |
| GAS (n) | A fluid that has no shape or volume and that can expand |  |
| gaseous (adj) | NOT APPROVED | use: GAS (n) — "The tool cylinder contains a gaseous mixture of 10% helium and 90% nitrogen." → "THE TOOL CYLINDER CONTAINS A MIXTURE OF GASES (10% HELIUM AND 90% NITROGEN)." |
| gash (v) | NOT APPROVED | use: DAMAGED (adj) — "If the thermal blanket is gashed, do repair No. 9." → "IF THE THERMAL BLANKET IS DAMAGED, DO REPAIR No. 9." |
| gather (v) | NOT APPROVED | use: COLLECT (v) — "All fluids gather at the lowest point in the compartment. Three computers gather data and parameters from the systems and put them together on the data link to the display unit." → "ALL FLUIDS COLLECT AT THE LOWEST POINT IN THE COMPARTMENT. THREE COMPUTERS COLLECT DATA AND PARAMETERS FROM THE SYSTEMS AND PUT THEM TOGETHER ON THE DATA LINK TO THE DISPLAY UNIT." |
| gauge (v) | NOT APPROVED | use: MEASURE (v) — "Gauge the width of the gap between the top edge and the bottom surface." → "MEASURE THE DISTANCE BETWEEN THE TOP EDGE AND THE BOTTOM SURFACE." |
| GENERAL (adj) | Of, or related to something as a whole, not detailed |  |
| generally (adv) | NOT APPROVED | use: USUALLY (adv) — "Memory modules are generally replaced during maintenance." → "YOU USUALLY REPLACE MEMORY MODULES DURING MAINTENANCE." |
| generate (v) | NOT APPROVED | use: BE (v); GIVE (v); SUPPLY (v) |
| generous (adj) | NOT APPROVED | use: LARGE (adj); THICK (adj) — If it is possible, be accurate. |
| generously (adv) | NOT APPROVED | use: LARGE (adj); THICK (adj) — If it is possible, be accurate. |
| gentle (adj) | NOT APPROVED | use: CAREFULLY (adv); LIGHTLY (adv) |
| gently (adv) | NOT APPROVED | use: CAREFULLY (adv); LIGHTLY (adv) |
| genuine (adj) | NOT APPROVED | use: CORRECT (adj) — "Make sure that the reading on the gauge is genuine." → "MAKE SURE THAT THE INDICATION ON THE GAUGE IS CORRECT." |
| GET (v) | To obtain, to come into the state of having | Do not use this word to mean BECOME, GO, DECREASE, INCREASE.; Refer to rule 9.2 and the entries from “get” until “get to” that follow.; forms: GETS, GOT No other verb forms. |
| get (v) | NOT APPROVED | use: BECOME (v) — "Do not let the heater get too hot." → "DO NOT LET THE HEATER BECOME TOO HOT." |
| get away (v) | NOT APPROVED | use: GO AWAY — "Get away from the exhaust area before the engine starts." → "BEFORE THE ENGINE STARTS, GO AWAY FROM THE EXHAUST AREA." |
| get down (v) | NOT APPROVED | use: DECREASE (v); GO DOWN |
| get into (v) | NOT APPROVED | use: GO INTO — "Install caps to make sure that foreign objects do not get into the receptacles." → "INSTALL CAPS ON THE RECEPTACLES TO MAKE SURE THAT UNWANTED MATERIAL DOES NOT GO INTO THE RECEPTACLES." |
| get off (v) | NOT APPROVED | use: MOVE OFF — "Before you move the ailerons, tell all persons to get off the wings." → "BEFORE YOU MOVE THE AILERONS, TELL ALL PERSONS TO MOVE OFF THE WINGS." |
| get to (v) | NOT APPROVED | use: BE (v); GO (v); INCREASE (v) |
| GIVE (v) | To provide | forms: GIVES, GAVE, GIVEN |
| gleam (v) | NOT APPROVED | use: SHINY (adj) — "Polish the surface with a soft cloth until it gleams." → "POLISH THE SURFACE WITH A SOFT CLOTH UNTIL IT BECOMES SHINY." |
| glitch (n) | NOT APPROVED | use: ERROR (n); FAILURE (TN); UNSERVICEABLE (adj) |
| gloss (n) | NOT APPROVED | use: SHINY (adj) — "Polish the surface to a high gloss." → "POLISH THE SURFACE UNTIL IT IS VERY SHINY." |
| GLOSSY (adj) | Smooth and shiny | forms: (GLOSSIER, GLOSSIEST) |
| glow (v) | NOT APPROVED | use: BE (v) — "Make sure that the indicator light glows. Adjust the potentiometer until the light glows dimly." → "MAKE SURE THAT THE INDICATOR LIGHT IS ON. ADJUST THE POTENTIOMETER UNTIL THE LIGHT IS DIM." |
| glue (v) | NOT APPROVED | use: BOND (v); ATTACH (v) |
| GO (v) | To move to or from something | forms: GOES, WENT No other verb forms. |
| GO OFF (v) | To become dark when an internal power source is de-energized | forms: GOES OFF, WENT OFF No other verb forms. |
| GOOD (adj) | That is satisfactory | forms: (BETTER, BEST) |
| gouge (v) | NOT APPROVED | use: GOUGE (TN) — "If the blade was gouged during removal, replace it." → "IF A GOUGE OCCURS IN THE BLADE DURING REMOVAL, REPLACE THE BLADE." |
| govern (v) | NOT APPROVED | use: CONTROL (v) — "This component governs the engine speed." → "THIS COMPONENT CONTROLS THE ENGINE SPEED." |
| grab (v) | NOT APPROVED | use: USE (v); HOLD (v) |
| gradient (n) | NOT APPROVED | use: SLOPE (n) — "When you park the vehicle on a gradient, put chocks on the wheels." → "WHEN YOU PARK THE VEHICLE ON A SLOPE, PUT CHOCKS ON THE WHEELS." |
| gradual (adj) | NOT APPROVED | use: GRADUALLY (adv) — "Make a gradual adjustment to the temperature." → "GRADUALLY ADJUST THE TEMPERATURE." |
| GRADUALLY (adv) | Slowly and continuously |  |
| graph (v) | NOT APPROVED | use: GRAPH (TN) — "Graph the test results." → "MAKE A GRAPH OF THE TEST RESULTS." |
| grasp (v) | NOT APPROVED | use: HOLD (v) — "Grasp the handle." → "HOLD THE HANDLE." |
| grave (adj) | NOT APPROVED | use: DANGEROUS (adj) — "Hydraulic fluid can cause grave skin problems." → "HYDRAULIC FLUID IS DANGEROUS FOR YOUR SKIN." |
| grease (v) | NOT APPROVED | use: LUBRICATE (v); GREASE (TN) |
| great (adj) | NOT APPROVED | use: LARGE (adj); MORE THAN; VERY (adv) |
| greatly (adv) | NOT APPROVED | use: VERY MUCH — "This method can greatly increase the risk of injury." → "THIS METHOD CAN INCREASE THE RISK OF INJURY VERY MUCH." |
| grip (n) | NOT APPROVED | use: HOLD (v) — "Make sure you have a tight grip of the jack body while turning it." → "HOLD THE JACK BODY TIGHTLY WHILE YOU TURN IT." |
| grip (v) | NOT APPROVED | use: HOLD (v) — "Grip the handle lightly with one hand." → "HOLD THE HANDLE LIGHTLY WITH ONE HAND." |
| GROOVE (n) | A long channel that is not wide |  |
| GROUND (n) | The surface of the earth |  |
| GROUND (v) | To connect to the ground or to a large object of zero potential | forms: GROUNDS, GROUNDED, GROUNDED |
| GROUP (n) | Objects that are related |  |
| grow (v) | NOT APPROVED | use: BECOME (v) — "If the battery grows too hot, disconnect it." → "IF THE BATTERY BECOMES TOO HOT, DISCONNECT IT." |
| guard (v) | NOT APPROVED | use: GUARD (TN) — "Make sure that the switches are guarded." → "MAKE SURE THAT THE GUARDS ARE INSTALLED ON THE SWITCHES." |
| guide (v) | NOT APPROVED | use: PUT (v); MOVE (v) |
| gush (v) | NOT APPROVED | use: FLOW (n) — "If you turn the valve handle to FULL, water will gush from the outlet." → "IF YOU TURN THE HANDLE TO “FULL,” THERE WILL BE A STRONG FLOW OF WATER FROM THE OUTLET." |
| halt (v) | NOT APPROVED | use: STOP (v) — "If you hear an unusual noise, halt the procedure." → "IF YOU HEAR AN UNUSUAL NOISE, STOP THE PROCEDURE." |
| halve (v) | NOT APPROVED | use: HALF (TN) — "Check that the deviation in pitch is halved." → "MAKE SURE THAT THE PITCH DECREASES TO HALF ITS VALUE." |
| hamper (v) | NOT APPROVED | use: PREVENT (v) — "Strong winds can hamper the correct deployment of the escape slides." → "STRONG WINDS CAN PREVENT THE CORRECT DEPLOYMENT OF THE ESCAPE SLIDES." |
| handle (v) | NOT APPROVED | use: MOVE (v); TOUCH (v); USE (v); CAREFUL (adj) — This word can be part of a safety sign (rule 8.6). |
| hand-tight (adj) | NOT APPROVED | use: YOUR HAND — TIGHTEN … WITH — "Install the filter case hand-tight." → "INSTALL THE FILTER CASE AND TIGHTEN IT WITH YOUR HAND." |
| hand-tighten (v) | NOT APPROVED | use: YOUR HAND — TIGHTEN … WITH — "Hand-tighten the swivel nut." → "TIGHTEN THE SWIVEL NUT WITH YOUR HAND." |
| HANG (v) | To attach or to be attached to something above with no support from below | forms: HANGS, HUNG, HUNG |
| happen (v) | NOT APPROVED | use: OCCUR (v) — "If an accident happens, get medical attention." → "IF AN ACCIDENT OCCURS, GET MEDICAL AID." |
| HARD (adj) | Not easy to cut, not easy to go into or through | forms: (HARDER, HARDEST) |
| harden (v) | NOT APPROVED | use: HARD (adj); CURE (TV) — Refer to rule 1.12. |
| harm (v) | NOT APPROVED | use: INJURY (n); IRRITATION (TN) — Refer to rule 1.5. |
| harmful (adj) | NOT APPROVED | use: DANGEROUS (adj); INJURY (n) |
| harmonize (v) | NOT APPROVED | use: AGREE (v); ALIGN (v) |
| haul (v) | NOT APPROVED | use: TOW (v); MOVE (v) |
| HAVE (v) | To possess as a part or quality | forms: HAS, HAD No other verb forms. |
| have to (v) | NOT APPROVED | Use a verb in the imperative form — "When engines are in operation, you have to put on a hearing protection device." → "WHEN ENGINES ARE IN OPERATION, PUT ON A HEARING PROTECTION DEVICE." |
| hazard (n) | NOT APPROVED | DANGEROUS (adj) “hazard” can be part of safety regulations. — "Trichloroethylene is a health hazard." → "TRICHLORO-ETHYLENE IS DANGEROUS." |
| hazardous (adj) | NOT APPROVED | DANGEROUS (adj) “hazardous” can be part of safety regulations. — "All personnel who work with hazardous materials must obey the following safety instructions." → "ALL PERSONNEL WHO DO WORK WITH DANGEROUS MATERIALS MUST OBEY THE SAFETY INSTRUCTIONS THAT FOLLOW." |
| hazy (adj) | NOT APPROVED | use: HAZE (TN) — "If the weather is hazy, do not do the test." → "IF THERE IS HAZE, DO NOT DO THE TEST." |
| HEAD (n) | The top of something |  |
| head (v) | NOT APPROVED | use: POINT (v) — "Head the aircraft into the wind." → "POINT THE AIRCRAFT INTO THE WIND." |
| HEAR (v) | To know by sound in the ear | forms: HEARS, HEARD, HEARD |
| HEAT (n) | The condition or quality of being hot |  |
| heat (v) | NOT APPROVED | use: HEAT (n); HOT (adj) |
| HEAVY (adj) | That has a large mass, weight, or force | forms: (HEAVIER, HEAVIEST) |
| HEIGHT (n) | The vertical distance |  |
| heighten (v) | NOT APPROVED | use: INCREASE (v) — "Strong winds will heighten the risk of damage." → "STRONG WINDS WILL INCREASE THE RISK OF DAMAGE." |
| help (n) | NOT APPROVED | use: AID (n) — "You must get medical help immediately." → "GET MEDICAL AID IMMEDIATELY." |
| HELP (v) | To make something easier or better | forms: HELPS, HELPED, HELPED |
| helpful (adj) | NOT APPROVED | use: HELP (v) — "Record the lockwire positions. This will be helpful during the assembly procedure." → "RECORD THE LOCKWIRE POSITIONS. THIS INFORMATION WILL HELP YOU DURING THE ASSEMBLY PROCEDURE." |
| HERE (adv) | In this position |  |
| hesitation (n) | NOT APPROVED | use: SMOOTHLY (adv); CORRECTLY (adv); IMMEDIATELY (adv) |
| HIGH (adj) | That is of large value | forms: (HIGHER, HIGHEST) |
| highly (adv) | NOT APPROVED | use: VERY (adv) — "Toluene is highly flammable." → "TOLUENE IS VERY FLAMMABLE." |
| hinder (v) | NOT APPROVED | use: PREVENT (v); DECREASE (v); BLOCKAGE (n); CLOGGED (adj) |
| hinge (v) | NOT APPROVED | use: TURN (v) — "Panels hinge on two nylon straps." → "THE PANELS TURN ON TWO NYLON STRAPS." |
| HIT (v) | To touch suddenly and with much force | forms: HITS, HIT, HIT |
| hitch (v) | NOT APPROVED | use: CONNECT (v) — "Hitch the towing arm to the nosewheel." → "CONNECT THE TOWING ARM TO THE NOSEWHEEL." |
| hoist (v) | NOT APPROVED | use: LIFT (v) — "Hoist the module." → "LIFT THE MODULE." |
| hold (n) | NOT APPROVED | use: HOLD (v) — "Make sure that you have a tight hold on the rod." → "MAKE SURE THAT YOU HOLD THE ROD TIGHTLY." |
| HOLD (v) | 1. To continue to have in the hand or grip 2. To continue to have in a specified location, position, or condition | forms: HOLDS, HELD, HELD |
| hold back (v) | NOT APPROVED | use: PREVENT (v) — "At full thrust, the brakes must hold the aircraft back." → "AT FULL THRUST, THE BRAKES MUST PREVENT MOVEMENT OF THE AIRCRAFT." |
| hold off (v) | NOT APPROVED | use: PREVENT (v) — "The protective paint will hold off corrosion for six months." → "THE PROTECTIVE PAINT WILL PREVENT CORROSION FOR SIX MONTHS." |
| HOLE (n) | An empty space in a solid object |  |
| hook (v) | NOT APPROVED | use: PUT (v) — "Hook the sling on the shackle." → "PUT THE SLING ON THE SHACKLE." |
| hook up (v) | NOT APPROVED | use: CONNECT (v) — "Hook the towing arm up to the nose gear." → "CONNECT THE TOWING ARM TO THE NOSE GEAR." |
| HORIZONTAL (adj) | Parallel to the horizon or a baseline |  |
| HORIZONTALLY (adv) | In a horizontal position |  |
| HOT (adj) | At a high temperature | forms: (HOTTER, HOTTEST) |
| house (v) | NOT APPROVED | use: CONTAIN (v) — "The module houses five components." → "THE MODULE CONTAINS FIVE COMPONENTS." |
| HOW (adv) | By which manner |  |
| however (adv) | NOT APPROVED | use: BUT (conj) — "The drying time is usually 24 hours. However, the procedure in this step will decrease the drying time to 12 hours." → "THE DRYING TIME IS USUALLY 24 HOURS. BUT THE PROCEDURE IN THIS STEP WILL DECREASE THE DRYING TIME TO 12 HOURS." |
| huge (adj) | NOT APPROVED | use: LARGE (adj) — "To remove the paint stripper, flush the surface with huge quantities of water." → "TO REMOVE THE PAINT STRIPPER, FLUSH THE SURFACE WITH LARGE QUANTITIES OF WATER." |
| hum (v) | NOT APPROVED | use: HUM (TN) — "Adjust the potentiometer until the loudspeaker no longer hums." → "ADJUST THE POTENTIOMETER UNTIL YOU DO NOT HEAR A HUM FROM THE LOUDSPEAKER." |
| hurt (v) | NOT APPROVED | use: INJURY (n) — "Be careful when you do this procedure. If the unit falls, it can hurt persons." → "BE CAREFUL WHEN YOU DO THIS PROCEDURE. IF THE UNIT FALLS, IT CAN CAUSE INJURY TO PERSONS." |
| HYDRAULIC (adj) | Related to, or operated by, pressurized liquid |  |
| HYDRAULICALLY (adv) | With hydraulic power |  |
| identical (adj) | NOT APPROVED | use: SAME (adj) — "The procedure is identical for both VHF sets." → "THE SAME PROCEDURE IS APPLICABLE TO THE TWO VHF SETS." |
| IDENTIFICATION (n) | Something that identifies an object |  |
| IDENTIFY (v) | 1. To use a specified code or marking to supply with an identity 2. To show an identity For other meanings, use: FIND (v) | forms: IDENTIFIES, IDENTIFIED, IDENTIFIED |
| idle (v) | NOT APPROVED | use: IDLE (TN) — "Idle the engine for 20 minutes." → "OPERATE THE ENGINE AT IDLE FOR 20 MINUTES." |
| IF (conj) | In the event that, on the condition that, in case of |  |
| ignite (v) | NOT APPROVED | use: IGNITION (TN) — "Fuel passes through the atomizers to the combustion chamber, where it is ignited." → "FUEL GOES THROUGH THE ATOMIZERS INTO THE COMBUSTION CHAMBER, WHERE IGNITION OCCURS." |
| IGNORE (v) | Not to think about something, not to do something about | forms: IGNORES, IGNORED, IGNORED |
| ILLUMINATE (v) | To make something visible with an external light source | For lights or lamps, use: COME ON BE ON; forms: ILLUMINATES, ILLUMINATED, ILLUMINATED |
| immediate (adj) | NOT APPROVED | use: IMMEDIATELY (adv) — "Check the speedbrake for immediate retraction." → "MAKE SURE THAT THE SPEEDBRAKE RETRACTS IMMEDIATELY." |
| IMMEDIATELY (adv) | Without a gap of time or space |  |
| immerse (v) | NOT APPROVED | use: SOAK (v); PUT FULLY INTO |
| immobilize (v) | NOT APPROVED | use: LOCK (v); PREVENT MOVEMENT |
| impact (n) | NOT APPROVED | use: HIT (v) — "Avoid impact between metal objects and the mating surface." → "MAKE SURE THAT METAL OBJECTS DO NOT HIT THE MATING SURFACE." |
| impact (v) | NOT APPROVED | use: HIT (v); EFFECT (n) |
| impair (v) | NOT APPROVED | use: DECREASE (v); OPERATE INCORRECTLY; CAUSE DAMAGE |
| implement (v) | NOT APPROVED | use: DO (v) — "If the test does not give satisfactory results, implement the fault isolation procedure." → "IF THE TEST DOES NOT GIVE SATISFACTORY RESULTS, DO THE FAULT ISOLATION PROCEDURE." |
| implementation (n) | NOT APPROVED | use: DO (v) — "The implementation of the procedure in this Service Bulletin is mandatory." → "IT IS MANDATORY TO DO THE PROCEDURE IN THIS SERVICE BULLETIN." |
| IMPORTANT (adj) | That has a significant effect |  |
| impossible (adj) | NOT APPROVED | use: NOT POSSIBLE; CANNOT (v) |
| impregnate (v) | NOT APPROVED | use: SOAK (v) — "The filter elements must be impregnated with oil." → "SOAK THE FILTER ELEMENTS IN OIL." |
| impression (n) | NOT APPROVED | use: THINK (v) — "If you have the impression that a tire has low pressure, do the steps that follow:" → "IF YOU THINK THAT A TIRE HAS LOW PRESSURE, DO THE STEPS THAT FOLLOW:" |
| improper (adj) | NOT APPROVED | use: INCORRECT (adj) — "Improper adjustment of the stop bolts on the rudder pedals can cause damage." → "INCORRECT ADJUSTMENT OF THE STOP BOLTS ON THE RUDDER PEDALS CAN CAUSE DAMAGE." |
| improperly (adv) | NOT APPROVED | use: INCORRECTLY (adv) — "If the hinge is improperly adjusted, the panel will not close." → "IF THE HINGE IS INCORRECTLY ADJUSTED, YOU CANNOT CLOSE THE PANEL." |
| improve (v) | NOT APPROVED | use: BETTER (adj) — "Do not readjust the parts to improve their position." → "DO NOT ADJUST THE PARTS AGAIN TO MAKE THEIR POSITION BETTER." |
| impurity (n) | NOT APPROVED | use: UNWANTED MATERIAL; CONTAMINATION (n) |
| IN (adv) | To, or into a location or position |  |
| IN (prep) | Function word that shows location, position, condition, time, or limits |  |
| IN FRONT OF (prep) | In a position ahead of |  |
| IN PROGRESS (adv) | Occurring |  |
| inactive (adj) | NOT APPROVED | use: NOT ACTIVE — "The autothrust system is engaged but inactive." → "THE AUTOTHRUST SYSTEM IS ENGAGED BUT IT IS NOT ACTIVE." |
| inadvertent (adj) | NOT APPROVED | use: ACCIDENTAL (adj) — "Inadvertent operation of the system could cause fatal injuries." → "ACCIDENTAL OPERATION OF THE SYSTEM CAN KILL YOU." |
| inadvertently (adv) | NOT APPROVED | use: ACCIDENTALLY (adv) — "If the tank is inadvertently overfilled, open the drain valve." → "IF YOU ACCIDENTALLY PUT TOO MUCH FUEL IN THE TANK, OPEN THE DRAIN VALVE." |
| INBOARD (adj) | Nearer to the longitudinal axis |  |
| INBOARD (adv) | In or to a position nearer to the longitudinal axis |  |
| INBOARD OF (prep) | At a position nearer to the longitudinal axis |  |
| INCIDENT (n) | An important occurrence that can cause damage or have dangerous results |  |
| incline (n) | NOT APPROVED | use: SLOPE (n) — "You can adjust the incline of the ramp." → "YOU CAN ADJUST THE SLOPE OF THE RAMP." |
| INCLUDE (v) | To make, or to be, part of | forms: INCLUDES, INCLUDED, INCLUDED |
| including (prep) | NOT APPROVED | use: THRU (prep); WITH (prep) |
| incompatible (adj) | NOT APPROVED | use: NOT COMPATIBLE — "This software is incompatible with other operating systems. This coolant is incompatible with aluminum alloys." → "THIS SOFTWARE IS NOT COMPATIBLE WITH OTHER OPERATING SYSTEMS. THIS COOLANT IS NOT COMPATIBLE WITH ALUMINUM ALLOYS." |
| incomplete (adj) | NOT APPROVED | use: NOT FULL; NOT COMPLETED; ALL (adj) |
| incorporate (v) | NOT APPROVED | use: INCLUDE (v); HAVE (v) |
| incorporation (n) | NOT APPROVED | use: INCLUDE (v) — "Incorporation of a second diode increased the reliability of the motor." → "THE MANUFACTURER INCLUDED A SECOND DIODE TO INCREASE THE RELIABILITY OF THE MOTOR." |
| INCORRECT (adj) | Not correct |  |
| INCORRECTLY (adv) | In an incorrect manner |  |
| increase (n) | NOT APPROVED | use: INCREASE (v) — "There must be an increase in temperature." → "THE TEMPERATURE MUST INCREASE." |
| INCREASE (v) | To make or become larger or higher in value | forms: INCREASES, INCREASED, INCREASED |
| INCREMENT (n) | One of a sequence of regular operations done one after the other, to increase or decrease an adjustable quantity |  |
| incur (v) | NOT APPROVED | use: CAUSE (v) — "Removal of the unit before 24 hours can incur damage." → "REMOVAL OF THE UNIT BEFORE 24 HOURS CAN CAUSE DAMAGE." |
| independent (adj) | NOT APPROVED | use: INDEPENDENTLY (adv) — "The operation of this unit is independent." → "THIS UNIT OPERATES INDEPENDENTLY." |
| INDEPENDENTLY (adv) | Without a relation with |  |
| indicate (v) | NOT APPROVED | use: SHOW (v); IDENTIFY (v); SPECIFIED (adj) |
| INDICATION (n) | Something that is shown |  |
| induce (v) | NOT APPROVED | use: CAUSE (v) — "Scratches in the windscreen may induce cracks." → "SCRATCHES IN THE WINDSCREEN CAN CAUSE CRACKS." |
| ineffective (adj) | NOT APPROVED | use: UNSERVICEABLE (adj); UNSATISFACTORY (adj); NOT OPERATE |
| inflammable (adj) | NOT APPROVED | use: FLAMMABLE (adj) — "Solvent is highly inflammable." → "SOLVENT IS VERY FLAMMABLE." |
| INFLATE (v) | To make or become larger as a result of pressurization by a gas | forms: INFLATES, INFLATED, INFLATED |
| inform (v) | NOT APPROVED | use: TELL (v) — "Inform the manufacturer about the problem." → "TELL THE MANUFACTURER ABOUT THE PROBLEM." |
| INFORMATION (n) | Data collected and made available for a specified function |  |
| ingest (v) | NOT APPROVED | use: SWALLOW (v) — "If you ingest hydraulic fluid, get medical aid immediately." → "IF YOU SWALLOW HYDRAULIC FLUID, GET MEDICAL AID IMMEDIATELY." |
| ingress (n) | NOT APPROVED | use: GO INTO — "Water ingress will damage the component." → "IF WATER GOES INTO THE COMPONENT, DAMAGE WILL OCCUR." |
| inhale (v) | NOT APPROVED | use: BREATHE (v) — "Do not inhale the solvent fumes." → "DO NOT BREATHE THE SOLVENT FUMES." |
| inhibit (v) | NOT APPROVED | use: PREVENT (v) — "Alodine inhibits corrosion." → "ALODINE PREVENTS CORROSION." |
| INITIAL (adj) | That is related to the start |  |
| INITIALLY (adv) | At the start |  |
| initiate (v) | NOT APPROVED | use: START (v) — "Initiate the test at 2000 rpm." → "START THE TEST AT 2000 RPM." |
| inject (v) | NOT APPROVED | use: PUT (v) — "Inject oil into the gearbox with a syringe." → "PUT OIL INTO THE GEARBOX WITH A SYRINGE." |
| injection (n) | NOT APPROVED | use: PUT (v) — "The injection of the corrosion preventive oil into the pump must be done with a syringe." → "PUT THE CORROSION PREVENTIVE OIL INTO THE PUMP WITH A SYRINGE." |
| injure (v) | NOT APPROVED | use: INJURY (n) — "Make sure that the end of the safety wire will not injure persons." → "MAKE SURE THAT THE END OF THE SAFETY WIRE WILL NOT CAUSE INJURY TO PERSONS." |
| INJURY (n) | Damage to a person |  |
| INNER (adj) | Nearer to the center of an object |  |
| inoperative (adj) | NOT APPROVED | use: OFF (adj); NOT OPERATE |
| INPUT (n) | The data, power, or energy put into equipment or a system |  |
| insert (v) | NOT APPROVED | use: PUT (v); ENGAGE (v) |
| inside (adj) | NOT APPROVED | use: INNER (adj) — "Clean the inside surface of the container." → "CLEAN THE INNER SURFACE OF THE CONTAINER." |
| inside (n) | NOT APPROVED | use: INNER (adj) — "Paint the inside surface of the pump assembly." → "PAINT THE INNER SURFACE OF THE PUMP ASSEMBLY." |
| inside (prep) | NOT APPROVED | use: IN (prep); INTO (prep) |
| inspect (v) | NOT APPROVED | use: EXAMINE (v); INSPECTION (n) |
| INSPECTION (n) | The procedure which compares an object with its standard or specification |  |
| INSTALL (v) | To attach an item in or to a second item | forms: INSTALLS, INSTALLED, INSTALLED |
| INSTALLATION (n) | The procedure which installs an item |  |
| instead (adv) | NOT APPROVED | use: ALTERNATIVE (n) — "Use a spatula instead." → "USE A SPATULA AS AN ALTERNATIVE." |
| instead of (prep) | NOT APPROVED | use: ALTERNATIVE (n) — "You can use a clean plastic bag instead of the specified container." → "YOU CAN USE A CLEAN PLASTIC BAG AS AN ALTERNATIVE TO THE SPECIFIED CONTAINER." |
| INSTRUCTION (n) | A command that you must obey |  |
| INSTRUMENT (n) | An item which measures and/or shows |  |
| insufficient (adj) | NOT APPROVED | use: NOT SUFFICIENT — "If this step is insufficient to stop the leakage, replace the actuator." → "IF THIS STEP IS NOT SUFFICIENT TO STOP THE LEAKAGE, REPLACE THE ACTUATOR." |
| INSULATION (n) | A material that helps to prevent the movement of energy |  |
| insure (v) | NOT APPROVED | use: MAKE SURE (v) — "Insure that the work bench is clean." → "MAKE SURE THAT THE WORK BENCH IS CLEAN." |
| intact (adj) | NOT APPROVED | use: NOT DAMAGED — "Make sure the windscreen is intact." → "MAKE SURE THAT THE WINDSCREEN IS NOT DAMAGED." |
| integral (adj) | NOT APPROVED | use: PART (n) — "The pin is integral with the pump." → "THE PIN IS A PART OF THE PUMP." |
| INTENSITY (n) | The quantity of strength, force, or energy |  |
| INTERCHANGE (v) | To put or use each of two things in the place of the other without change | forms: INTERCHANGES, INTERCHANGED, INTERCHANGED |
| INTERCHANGEABLE (adj) | That you can interchange |  |
| interconnect (v) | NOT APPROVED | use: CONNECT (v) — "The pipes interconnect system A and system B." → "THE PIPES CONNECT SYSTEM A TO SYSTEM B." |
| INTERFACE (n) | The connection between two systems or components |  |
| interfere (v) | NOT APPROVED | use: HIT (v); CATCH (v); TOUCH (v); INTERFERENCE (TN) |
| interference (n) | NOT APPROVED | use: HIT (v); CATCH (v); TOUCH (v) — This word can be a technical noun or part of a technical noun. |
| interior (n) | NOT APPROVED | use: INTERNALLY (adv); INTERNAL (adj) |
| intermediate (adj) | NOT APPROVED | use: MIDDLE (adj); BETWEEN (prep) — Give the limits. |
| INTERMITTENT (adj) | That stops and starts again, not continuous |  |
| INTERMITTENTLY (adv) | In an intermittent manner |  |
| INTERNAL (adj) | Of, or on, the inner side and inner space |  |
| INTERNALLY (adv) | Of, or on, the inner side and inner space |  |
| interrupt (v) | NOT APPROVED | use: STOP (v) — "Do not interrupt the test." → "DO NOT STOP THE TEST." |
| intersect (v) | NOT APPROVED | use: INTERSECTION (TN) — "Drill a hole where the two lines intersect." → "DRILL A HOLE AT THE INTERSECTION OF THE TWO LINES." |
| INTERVAL (n) | A distance or gap between two points in space or time |  |
| INTO (prep) | 1. Movement to something and access to it 2. Function word that shows change, condition, result |  |
| investigate (v) | NOT APPROVED | use: INVESTIGATION (n) — "Investigate the cause of the fuel leakage." → "DO AN INVESTIGATION TO FIND THE CAUSE OF THE FUEL LEAKAGE." |
| INVESTIGATION (n) | An official and accurate inquiry or research |  |
| inward (adj) | NOT APPROVED | use: INNER (adj) — "Measure the inward diameter of the hole." → "MEASURE THE INNER DIAMETER OF THE HOLE." |
| inward (adv) | NOT APPROVED | use: IN (adv) — "Move the door inward and rearward." → "MOVE THE DOOR IN AND REARWARD." |
| IRREGULAR (adj) | Not regular |  |
| irregularity (n) | NOT APPROVED | use: DAMAGE (n); DEFECT (TN); IRREGULAR (adj); UNUSUAL (adj) |
| IRREGULARLY (adv) | Not regularly |  |
| ISOLATE (v) | To prevent a supply or connection to | forms: ISOLATES, ISOLATED, ISOLATED |
| isolation (n) | NOT APPROVED | use: ISOLATE (v) — "Isolation of system No. 1 is necessary to do the leakage checks." → "ISOLATE SYSTEM No. 1 TO DO THE LEAKAGE CHECKS." |
| IT (pron) | 1. That refers to a thing that was previously mentioned 2. That refers to an explicit or implicit state of affairs or circumstances |  |
| ITEM (n) | A thing that is determined or specified |  |
| ITS (adj) | Belonging to a thing |  |
| jack (v) | NOT APPROVED | use: JACK (TN) — "Do not jack the aircraft if the wind speed exceeds 20 mph." → "DO NOT LIFT THE AIRCRAFT ON JACKS IF THE WIND SPEED IS MORE THAN 20 MPH." |
| jam (v) | NOT APPROVED | use: FREELY (adv) — "Check that the valve spindle does not bind or jam." → "MAKE SURE THAT THE VALVE SPINDLE MOVES FREELY." |
| job (n) | NOT APPROVED | use: WORK (n); TASK (n) |
| join (v) | NOT APPROVED | use: BOND (v); ATTACH (v); CONNECT (v) |
| JOINT (n) | The area at which two surfaces or edges touch or are attached |  |
| just (adv) | NOT APPROVED | use: IMMEDIATELY (adv) — "Keep the ring just above the jack collars." → "KEEP THE RING IMMEDIATELY ABOVE THE JACK COLLARS." |
| KEEP (v) | To continue to have or hold | forms: KEEPS, KEPT, KEPT |
| key (v) | NOT APPROVED | use: REFER (v); KEY (TN) |
| KILL (v) | To cause death | forms: KILLS, KILLED, KILLED |
| kind (n) | NOT APPROVED | use: TYPE (n) — "Two kinds of sealing compound can be used." → "YOU CAN USE TWO TYPES OF SEALING COMPOUND." |
| kink (v) | NOT APPROVED | use: KINK (TN) — "Do not kink the cables." → "DO NOT MAKE KINKS IN THE CABLES." |
| knock (v) | NOT APPROVED | use: HIT (v) — "Knock the clamp on the right side with a hammer." → "HIT THE CLAMP ON THE RIGHT SIDE WITH A HAMMER." |
| KNOW (v) | To be sure of data, to have data ready to use | forms: KNOWS, KNEW, KNOWN |
| label (v) | NOT APPROVED | use: IDENTIFY (v); LABEL (TN) |
| lack (n) | NOT APPROVED | use: NOT SUFFICIENT — "Damage can occur to the pump if there is a lack of oil in the reservoir." → "DAMAGE CAN OCCUR TO THE PUMP IF THERE IS NOT SUFFICIENT OIL IN THE RESERVOIR." |
| LAMINATED (adj) | Made of laminations |  |
| LAMINATION (n) | Layers of one or more materials bonded together |  |
| land (v) | NOT APPROVED | use: LANDING (TN) — "If the aircraft landed heavily, do the Heavy Landing Inspection." → "AFTER A HEAVY LANDING, DO THE HEAVY LANDING INSPECTION." |
| LARGE (adj) | More than average in dimension, quantity, or capacity | forms: (LARGER, LARGEST) |
| LAST (adj) | That comes at the end |  |
| LAST (adv) | After other persons or things |  |
| last (v) | NOT APPROVED | use: CONTINUE (v) — "The signals last 0.8 seconds." → "THE SIGNALS CONTINUE FOR 0.8 SECONDS." |
| LATCH (v) | To hold something in position with a latching device | forms: LATCHES, LATCHED, LATCHED |
| later (adj) | NOT APPROVED | use: SUBSEQUENT (adj); THEN (adv) |
| later (adv) | NOT APPROVED | use: SUBSEQUENTLY (adv); WHEN (conj); AFTER (prep) — If it is possible, give the condition or time. |
| LATERAL (adj) | Related to or on the side |  |
| LATERALLY (adv) | In a lateral direction |  |
| lay (v) | NOT APPROVED | use: PUT (v) — "Lay covers on the floor." → "PUT COVERS ON THE FLOOR." |
| LAYER (n) | A material applied to a surface or put on, or below, a second material |  |
| lead (v) | NOT APPROVED | use: PUT (v) — "Lead the Teleflex cable through the bulkhead." → "PUT THE TELEFLEX CABLE THROUGH THE BULKHEAD." |
| LEAK (n) | A crack, gap or hole which lets fluid or light go into or come out of something |  |
| leak (v) | NOT APPROVED | use: LEAK (n) — "If the system is leaking, repair it." → "IF THERE ARE LEAKS IN THE SYSTEM, REPAIR THEM." |
| LEAKAGE (n) | The quantity of material that goes through a leak |  |
| least (adv) | NOT APPROVED | use: MINIMUM (adj) — "Repair the least damaged area first." → "REPAIR THE AREA WITH THE MINIMUM DAMAGE FIRST." |
| least (at least) (adv) | NOT APPROVED | use: MINIMUM (adj); MINIMUM (n) |
| leave (v) | NOT APPROVED | use: KEEP (v); GO (v) — LET …. STAY (v) |
| LEFT (adj) | On the west side when you look north |  |
| left-hand (adj) | NOT APPROVED | use: LEFT (adj) — "Set the left-hand switch to ON." → "SET THE LEFT SWITCH TO “ON.”" |
| legible (adj) | NOT APPROVED | use: READ (v) — "Make certain that the identification plates are legible." → "MAKE SURE THAT YOU CAN READ THE IDENTIFICATION PLATES." |
| LENGTH (n) | 1. The distance from one end to the other end 2. The longer or longest of the three dimensions of an object |  |
| lengthen (v) | NOT APPROVED | use: INCREASE (v) — "Do not try to lengthen this rod." → "DO NOT TRY TO INCREASE THE LENGTH OF THIS ROD." |
| LESS (adj) | Of smaller dimension, value, quantity, volume, or number | forms: No other forms of this adjective. |
| LET (v) | To give opportunity | forms: LETS, LET No other verb forms. |
| lethal (adj) | NOT APPROVED | use: KILL (v) — "The electrical discharge from these power units can be lethal." → "THE ELECTRICAL DISCHARGE FROM THESE POWER UNITS CAN KILL YOU." |
| LEVEL (adj) | Horizontal to a known datum |  |
| LEVEL (n) | A horizontal line, plane, surface, or condition |  |
| level (v) | NOT APPROVED | use: LEVEL (adj) — "Level the aircraft." → "MAKE THE AIRCRAFT LEVEL." |
| liberal (adj) | NOT APPROVED | use: LARGE (adj); THICK (adj) |
| liberally (adv) | NOT APPROVED | use: LARGE (adj); THICK (adj) |
| lie (v) | NOT APPROVED | use: BE (v) — "The other part of the clip lies along the barrel." → "THE OTHER PART OF THE CLIP IS ALONG THE BARREL." |
| LIFE (n) | The time during which you can use an item or object |  |
| LIFT (v) | To move something up | forms: LIFTS, LIFTED, LIFTED |
| LIGHT (adj) | That has a small mass, weight, or force | For other meanings, use: THIN (adj); SMALL (adj); forms: (LIGHTER, LIGHTEST) |
| light (v) | NOT APPROVED | use: COME ON — "Ensure that the fluid indicator light lights." → "MAKE SURE THAT THE FLUID INDICATOR LIGHT COMES ON." |
| LIGHTING (n) | That which gives light to |  |
| LIGHTLY (adv) | In a light manner |  |
| LIMIT (n) | A specified maximum or minimum quantity, number, time, or distance |  |
| limitation (n) | NOT APPROVED | use: LIMIT (n) — "When you lift the aircraft on jacks, observe these center of gravity limitations:" → "WHEN YOU LIFT THE AIRCRAFT ON JACKS, KEEP THE CENTER OF GRAVITY BETWEEN THESE LIMITS:" |
| limited (adj) | NOT APPROVED | use: SMALL (adj) — "There is only a limited number of repairs that you can do." → "THERE IS ONLY A SMALL NUMBER OF REPAIRS THAT YOU CAN DO." |
| LINEAR (adj) | In a straight line |  |
| LINEARLY (adv) | In a straight line |  |
| link (v) | NOT APPROVED | use: CONNECT (v); ATTACH (v) |
| LIQUID (adj) | That has the properties of a liquid |  |
| LIQUID (n) | A material that is not a gas or a solid |  |
| list (v) | NOT APPROVED | use: RECORD (v); SHOW (v); LIST (TN) |
| LISTEN (v) | To use your ears to hear or find | forms: LISTENS, LISTENED, LISTENED |
| little (adj) | NOT APPROVED | use: SMALL (adj); SHORT (adj); NOT SUFFICIENT |
| little (a little) (adj) | NOT APPROVED | use: SMALL QUANTITY — "Add a little disinfectant to the solution." → "ADD A SMALL QUANTITY OF DISINFECTANT TO THE SOLUTION." |
| little (a little) (adv) | NOT APPROVED | use: SMALL (adj) — "After you remove the nut, the rib can move down a little." → "AFTER YOU REMOVE THE NUT, THE RIB CAN MOVE DOWN A SMALL DISTANCE." |
| LIVE (adj) | That includes explosive material | For electrical systems, use: ENERGIZE (v) |
| load (v) | NOT APPROVED | use: INSTALL (v); LOAD (TN) |
| LOCAL (adj) | Applicable to a given location or position |  |
| LOCALLY (adv) | Applicable to a given location or position |  |
| locate (v) | NOT APPROVED | use: FIND (v); ENGAGE (v); PUT (v) |
| LOCATION (n) | A place or site that you can find |  |
| LOCK (v) | To attach something, or hold it in position with a locking device | forms: LOCKS, LOCKED, LOCKED |
| log (v) | NOT APPROVED | use: RECORD (v) — "Log the compass corrections on the card." → "RECORD THE COMPASS CORRECTIONS ON THE CARD." |
| LONG (adj) | That has a specified or large length, or a specified or large duration | forms: (LONGER, LONGEST) |
| long (as long as) (conj) | NOT APPROVED | use: WHILE (conj) — "As long as the DC supply is ON, the fan must operate." → "WHILE THE DC SUPPLY IS ON, THE FAN MUST OPERATE." |
| long (no longer) (adv) | NOT APPROVED | NOT… AT THIS TIME UNTIL…NOT — "This procedure is no longer applicable. Adjust the potentiometer until the loudspeaker no longer hums." → "THIS PROCEDURE IS NOT APPLICABLE AT THIS TIME. ADJUST THE POTENTIOMETER UNTIL YOU DO NOT HEAR A HUM FROM THE LOUDSPEAKER." |
| LONGITUDINAL (adj) | Related to the longitudinal axis |  |
| LONGITUDINALLY (adv) | In a longitudinal direction |  |
| LOOK (v) | To use your eyes to see or find | forms: LOOKS, LOOKED, LOOKED |
| LOOP (n) | A circular shape made in a flexible material |  |
| loop (v) | NOT APPROVED | use: LOOP (n) — "Loop the wire around the unit." → "MAKE A LOOP OF WIRE AROUND THE UNIT." |
| LOOSE (adj) | 1. On, in, but not attached 2. Not tight | For other meanings, use: TENSION (TN) |
| LOOSELY (adv) | Not tightly |  |
| LOOSEN (v) | To cause to be not tight | forms: LOOSENS, LOOSENED, LOOSENED |
| lose (v) | NOT APPROVED | use: DECREASE (v) — "The solvent loses its effectiveness quickly." → "THE EFFECT OF THE SOLVENT DECREASES QUICKLY." |
| lost (adj) | NOT APPROVED | use: DECREASE (v); NOT FIND |
| LOW (adj) | That is of small value | forms: (LOWER, LOWEST) |
| LOWER (v) | To move something down | forms: LOWERS, LOWERED, LOWERED |
| lowermost (adj) | NOT APPROVED | use: BOTTOM (adj) — "The lowermost mark on the board is red." → "THE BOTTOM MARK ON THE BOARD IS RED." |
| LUBRICATE (v) | To apply lubricant | forms: LUBRICATES, LUBRICATED, LUBRICATED |
| lukewarm (adj) | NOT APPROVED | use: WARM (adj) — "Soak the area with lukewarm water." → "SOAK THE AREA WITH WARM WATER." |
| MAGNETIC (adj) | Related to the properties of a magnet |  |
| MAGNETICALLY (adv) | In a magnetic manner |  |
| main (adj) | NOT APPROVED | use: PRIMARY (adj) — "The main cause of valve failure is contamination of the fluid." → "THE PRIMARY CAUSE OF VALVE FAILURE IS CONTAMINATION OF THE FLUID." |
| maintain (v) | NOT APPROVED | use: KEEP (v); HOLD (v); MAINTENANCE (n) |
| MAINTENANCE (n) | The servicing and/or the repair of something to keep it in the correct condition |  |
| major (adj) | NOT APPROVED | use: PRIMARY (adj) — "The major function of the power unit is to supply electrical power." → "THE PRIMARY FUNCTION OF THE POWER UNIT IS TO SUPPLY ELECTRICAL POWER." |
| MAKE (v) | To manufacture, to cause to occur or to become | forms: MAKES, MADE, MADE |
| make certain (v) | NOT APPROVED | use: MAKE SURE (v) — "Make certain that the valve is open." → "MAKE SURE THAT THE VALVE IS OPEN." |
| MAKE SURE (v) | To verify and/or do the necessary steps | forms: MAKES SURE, MADE SURE, MADE SURE |
| maladjusted (adj) | NOT APPROVED | use: INCORRECTLY ADJUSTED — "If the warning light is on when the door is closed, the microswitch is maladjusted." → "IF THE WARNING LIGHT IS ON WHEN THE DOOR IS CLOSED, THE MICROSWITCH IS INCORRECTLY ADJUSTED." |
| MALFUNCTION (n) | Incorrect operation |  |
| MANDATORY (adj) | That which you must do, use, or obey If you want to use this word in procedures, think about a necessary safety instruction. |  |
| manipulate (v) | NOT APPROVED | use: MOVE (v); ADJUST (v) |
| MANUAL (adj) | Operated with the hands |  |
| MANUAL (n) | A publication that gives data related to a special subject |  |
| MANUALLY (adv) | With your hands |  |
| manufacture (v) | NOT APPROVED | use: MAKE (v) — "The clearing tool can be manufactured locally." → "YOU CAN MAKE THE CLEARING TOOL LOCALLY." |
| MANY (adj) | Of a large number If it is possible, give the range, number, or quantity. | forms: (MORE, MOST) |
| MARK (n) | Something that you make or is made to show an identification, location, or direction |  |
| mark (v) | NOT APPROVED | use: IDENTIFY (v); MARK (n) |
| mask (v) | NOT APPROVED | use: APPLY (v) — "Mask the transparent panel with masking tape." → "APPLY MASKING TAPE TO THE TRANSPARENT PANEL." |
| MASS (n) | The quantity of matter that is in an object and relates to its weight. The equivalent of inertia |  |
| match (v) | NOT APPROVED | use: ALIGN (v); AGREE (v) |
| mate (v) | NOT APPROVED | use: CONNECT (v); ENGAGE (v); TOGETHER (adv) |
| MATERIAL (n) | A substance from which an item is made, or an item that is necessary to do a task. |  |
| MATING (adj) | Made to touch |  |
| MATT (or MATTE) (adj) | NOT APPROVED | Not glossy |
| matter (n) | NOT APPROVED | use: MATERIAL (n) — "Remove the glossy matter from the surface of the blade." → "REMOVE THE GLOSSY MATERIAL FROM THE SURFACE OF THE BLADE." |
| MAXIMUM (adj) | Related to the largest dimension, quantity, number, or value |  |
| MAXIMUM (n) | The largest dimension, quantity, number, or value |  |
| may (v) | NOT APPROVED | use: CAN (v); POSSIBLY (adv) |
| MEASURE (v) | To find the dimensions, capacity, or quantity of something | forms: MEASURES, MEASURED, MEASURED |
| MECHANICAL (adj) | Related to or operated with a mechanism |  |
| MECHANICALLY (adv) | In a mechanical manner |  |
| MECHANISM (n) | An assembly of mechanical parts that are made to operate together |  |
| MEDICAL (adj) | Related to medicine |  |
| medium (adj) | NOT APPROVED | use: MODERATE (adj) — "A medium amount of pressure must be applied." → "APPLY MODERATE PRESSURE." |
| meet (v) | NOT APPROVED | use: ENGAGE (v); TOUCH (v) |
| MELT (v) | To change or to cause something to change from solid to liquid because of heat | forms: MELTS, MELTED, MELTED |
| mention (v) | NOT APPROVED | use: GIVE (v) — "The repair limits are not mentioned as special equipment is required." → "THE REPAIR LIMITS ARE NOT GIVEN BECAUSE SPECIAL EQUIPMENT IS NECESSARY." |
| mesh (v) | NOT APPROVED | use: ENGAGE (v) — "If the gears do not mesh correctly, add a shim." → "IF THE GEARS DO NOT ENGAGE CORRECTLY, ADD A SHIM." |
| meteorological (adj) | NOT APPROVED | use: WEATHER (n) — "Carry out the test in good meteorological conditions." → "DO THE TEST IN GOOD WEATHER." |
| METHOD (n) | A special type of procedure used to get a specified result |  |
| mid (adj) | NOT APPROVED | use: MIDDLE (adj) — "Place the throttle lever in mid position." → "PUT THE THROTTLE LEVER IN THE MIDDLE POSITION." |
| MIDDLE (adj) | At a point that is between two other points |  |
| MIDDLE (n) | A point that is at or near the center |  |
| mild (adj) | NOT APPROVED | use: WEAK (adj) — "Use a mild soap solution to clean the sidewall panel." → "USE A WEAK SOAP SOLUTION TO CLEAN THE SIDEWALL PANEL." |
| minimize (v) | NOT APPROVED | use: MINIMUM (n) — "Use a trestle to minimize the loads on the wing." → "USE A TRESTLE TO KEEP THE LOADS ON THE WING TO A MINIMUM." |
| MINIMUM (adj) | Related to the smallest dimension, quantity, number, or value |  |
| MINIMUM (n) | The smallest dimension, quantity, number, or value |  |
| minor (adj) | NOT APPROVED | use: SMALL (adj) — "Minor differences in temperature can be ignored." → "YOU CAN IGNORE SMALL DIFFERENCES IN TEMPERATURE." |
| MINUS (prep) | With the subtraction of |  |
| miscellaneous (adj) | NOT APPROVED | use: OTHER (adj); ALL (adj) |
| misrigged (adj) | NOT APPROVED | use: INCORRECTLY ADJUSTED — "If the marks are not aligned, the linkage is misrigged." → "IF THE MARKS ARE NOT ALIGNED, THE LINKAGE IS INCORRECTLY ADJUSTED." |
| MISSING (adj) | That is not there |  |
| mix (n) | NOT APPROVED | use: MIXTURE (n) — "The potlife of the mix is approximately 4 hours." → "THE POTLIFE OF THE MIXTURE IS APPROXIMATELY 4 HOURS." |
| MIX (v) | 1. To put together two or more materials to become one 2. To become combined | forms: MIXES, MIXED, MIXED |
| MIXTURE (n) | The result that you get when you mix materials |  |
| MOBILE (adj) | That is made to move easily |  |
| MODE (n) | A special condition of operation |  |
| MODERATE (adj) | Between low and high values |  |
| MODERATELY (adv) | In a moderate manner |  |
| modify (v) | NOT APPROVED | use: CHANGE (v); MODIFICATION (TN) |
| MOIST (adj) | Moderately wet |  |
| moisten (v) | NOT APPROVED | use: MOIST (adj) — "Moisten the cloth with solvent." → "MAKE THE CLOTH MOIST WITH SOLVENT." |
| MOMENTARILY (adv) | For a short time |  |
| momentary (adj) | NOT APPROVED | use: MOMENTARILY (adv) — "Check for momentary increase in speed." → "MAKE SURE THAT THE SPEED INCREASES MOMENTARILY." |
| MONITOR (v) | To do a check at something for a period of time to find if there is a change | forms: MONITORS, MONITORED, MONITORED |
| MOOR (v) | To hold something in position with ropes and cables | forms: MOORS, MOORED, MOORED |
| MORE (adj) | A large quantity of |  |
| MORE (adv) | To a larger degree |  |
| MOST (adj) | To the largest quantity of |  |
| MOST (adv) | To the largest degree |  |
| motion (n) | NOT APPROVED | use: MOVEMENT (n) — "Check that the stabilizer motion continues." → "MAKE SURE THAT THE STABILIZER MOVEMENT CONTINUES." |
| motor (v) | NOT APPROVED | use: DRY-MOTOR (TV); WET-MOTOR (TV); MOTORING (TN) |
| mount (v) | NOT APPROVED | use: INSTALL (v); ATTACH (v); PUT (v) |
| MOVABLE (adj) | That can move if necessary |  |
| MOVE (v) | To change or cause to change position or location | forms: MOVES, MOVED, MOVED |
| MOVEMENT (n) | A change of position or location |  |
| MUCH (adj) | Of relatively large dimension, value, quantity, or volume | forms: (MORE, MOST) |
| MUCH (adv) | To a great degree or extent |  |
| MULTIPLY (v) | To use multiplication to get a result For other meanings, use: INCREASE (v) | forms: MULTIPLIES, MULTIPLIED, MULTIPLIED |
| MUST (v) | Auxiliary modal verb that shows obligation |  |
| NAME (n) | The identification you give to a person or an object |  |
| NEAR (adj) | At or to a relatively short distance | forms: (NEARER, NEAREST) |
| NEAR (prep) | Approaching in space or condition |  |
| nearly (adv) | NOT APPROVED | use: ALMOST (adv) — "Move the pointer until nearly in the green band." → "MOVE THE POINTER UNTIL IT IS ALMOST IN THE GREEN BAND." |
| NECESSARY (adj) | That must be |  |
| need (v) | NOT APPROVED | use: NECESSARY (adj) — "The backing rings do not need to be replaced during this procedure." → "DURING THIS PROCEDURE, IT IS NOT NECESSARY TO REPLACE THE BACKING RINGS." |
| neither (adj) | NOT APPROVED | TWO (TN) … NOT — "Neither unit must operate." → "THE TWO UNITS MUST NOT OPERATE." |
| neither (pron) | NOT APPROVED | TWO (TN) … NOT — "Neither of the units must operate." → "THE TWO UNITS MUST NOT OPERATE." |
| NEUTRAL (adj) | 1. That has no effect 2. That is not acid or alkaline |  |
| neutralize (v) | NOT APPROVED | use: NEUTRAL (adj) — "Neutralize the basic electrolyte with vinegar or boric acid." → "MAKE THE BASIC ELECTROLYTE NEUTRAL WITH VINEGAR OR BORIC ACID." |
| never (adv) | NOT APPROVED | use: DO NOT — "Never allow the level in the tank to drop below half." → "DO NOT LET THE LEVEL IN THE TANK DECREASE TO LESS THAN HALF." |
| NEW (adj) | Not used before | forms: (NEWER, NEWEST) |
| NEXT (adj) | The first occurrence that follows immediately after in time or sequence. |  |
| next (adv) | NOT APPROVED | use: THEN (adv) — "Hold the flange in its position. Next, install the bolt." → "HOLD THE FLANGE IN ITS POSITION. THEN, INSTALL THE BOLT." |
| next to (prep) | NOT APPROVED | use: ADJACENT TO (prep) — "The pump is next to the central rib." → "THE PUMP IS ADJACENT TO THE CENTRAL RIB." |
| NO (adj) | Not any |  |
| NO (adv) | Function word that shows the negative answer to a question |  |
| NOISE (n) | An unwanted sound |  |
| noisy (adj) | NOT APPROVED | use: NOISE (n) — "If pump operation is noisy, check the pump filter for unwanted particles." → "IF THERE IS NOISE WHEN THE PUMP OPERATES, EXAMINE THE FILTER FOR UNWANTED PARTICLES." |
| NONE (pron) | Not one, not anyone |  |
| nor (conj) | NOT APPROVED | use: NOT (adv) — "In these conditions, neither the mechanical nor the electrical pitch trim systems will operate." → "IN THESE CONDITIONS, THE MECHANICAL AND ELECTRICAL PITCH TRIM SYSTEMS WILL NOT OPERATE." |
| normal (adj) | NOT APPROVED | use: USUAL (adj); CORRECT (adj) |
| normally (adv) | NOT APPROVED | use: USUALLY (adv); CORRECTLY (adv) |
| NOSE (n) | The front end or part, a part that protrudes |  |
| NOT (adv) | Adverb of negation |  |
| NOTCH (n) | An area in the shape of a “V” |  |
| note (v) | NOT APPROVED | use: RECORD (v) — "Note dimension A." → "RECORD DIMENSION “A.”" |
| notify (v) | NOT APPROVED | use: TELL (v); CONTACT (v); WRITE (v) |
| now (adv) | NOT APPROVED | use: AT THIS TIME — "Do not tighten the nuts now." → "DO NOT TIGHTEN THE NUTS AT THIS TIME." |
| NUMBER (n) | 1. A symbol or word that identifies an integer and/or decimal 2. An amount that you can count or calculate |  |
| OBEY (v) | To do that which the procedures or instructions tell you | forms: OBEYS, OBEYED, OBEYED |
| OBJECT (n) | Something that you can see or touch |  |
| observe (v) | NOT APPROVED | use: MONITOR (v); SEE (v); OBEY (v) |
| obstruct (v) | NOT APPROVED | use: CATCH (v); PREVENT (v); BLOCKAGE (n) |
| obstructed (adj) | NOT APPROVED | use: BLOCKED (adj); CLOGGED (adj) |
| obstruction (n) | NOT APPROVED | use: BLOCKAGE (n) — "Examine the drain holes for obstruction." → "EXAMINE THE DRAIN HOLES FOR BLOCKAGE." |
| obtain (v) | NOT APPROVED | use: GET (v) — "Add 0.05 mm to obtain the correct clearance for a standard spherical coupling." → "ADD 0.05 mm TO GET THE CORRECT CLEARANCE FOR A STANDARD SPHERICAL COUPLING." |
| OCCUR (v) | To be found or to take place, to come to be | forms: OCCURS OCCURRED |
| OF (prep) | Function word that shows: from, belonging to, having, or containing |  |
| OFF (adj) | Not in operation |  |
| OFF (adv) | 1. Not in operation 2. Not in contact |  |
| OFF (prep) | Not in contact with |  |
| often (adv) | NOT APPROVED | use: FREQUENTLY (adv) — "If a failure occurs often, do the system test." → "IF A FAILURE OCCURS FREQUENTLY, DO THE SYSTEM TEST." |
| oil (v) | NOT APPROVED | use: LUBRICATE (v); OIL (TN) |
| oil-free (adj) | NOT APPROVED | use: OIL (TN) — "Use an oil-free solution." → "USE A SOLUTION THAT CONTAINS NO OIL." |
| old (adj) | NOT APPROVED | use: REMAINING (adj); USED (adj); EXPIRED (adj) |
| omit (v) | NOT APPROVED | use: DO NOT DO; IGNORE (v) |
| ON (adj) | In operation |  |
| ON (adv) | 1. In operation 2. In contact |  |
| ON (prep) | Function word that shows contact, support, direction |  |
| once (adv) | NOT APPROVED | ONE (TN) TIME — "Press the switch once." → "PUSH THE SWITCH ONE TIME." |
| once (conj) | NOT APPROVED | use: WHEN (conj) — "Once the unit is on its mounting, lock it." → "WHEN THE UNIT IS ON ITS MOUNTING, LOCK IT." |
| ONE (pron) | That refers to a single person or object You can also use this word as a technical noun. |  |
| ONLY (adj) | Nothing more or different |  |
| ONLY (adv) | Exclusively |  |
| ONTO (prep) | To a position on or upon |  |
| opaque (adj) | NOT APPROVED | use: NOT TRANSPARENT — "Clean the opaque plastic surfaces." → "CLEAN THE PLASTIC SURFACES THAT ARE NOT TRANSPARENT." |
| OPEN (adj) | That lets something go in or out |  |
| OPEN (v) | 1. To move or cause to move from the closed position 2. To operate a circuit breaker to interrupt an electrical circuit | forms: OPENS, OPENED, OPENED |
| OPENING (n) | An aperture or hole in a surface |  |
| operable (adj) | NOT APPROVED | use: OPERATE (v) — "Make sure that the valve is operable. Check that the valve is operable." → "MAKE SURE THAT THE VALVE CAN OPERATE. MAKE SURE THAT YOU CAN OPERATE THE VALVE." |
| OPERATE (v) | To put, keep, or be in action | forms: OPERATES, OPERATED, OPERATED |
| OPERATION (n) | That which occurs when something operates or is operated |  |
| operational (adj) | NOT APPROVED | use: SERVICEABLE (adj); OPERATE (v) — This word can be part of a technical noun. |
| opportunity (n) | NOT APPROVED | If it is possible, be accurate. — "Replace the unit at the first opportunity." → "REPLACE THE UNIT AT THE NEXT CHECK." |
| OPPOSITE (adj) | 1. In the other direction 2. Across from |  |
| OPPOSITE (prep) | Across from |  |
| option (n) | NOT APPROVED | use: ALTERNATIVE (n); POSSIBLE (adj); CAN (v) |
| OPTIONAL (adj) | Not mandatory |  |
| OR (conj) | Function word that shows a choice | Do not use this word with the meaning of otherwise. Use a different construction. |
| order (n) | NOT APPROVED | use: SEQUENCE (n) — "Do the weighing procedure in the following order:" → "DO THE WEIGHING PROCEDURE IN THIS SEQUENCE:" |
| order (v) | NOT APPROVED | use: TELL (v); ORDER (TN) |
| orient (v) | NOT APPROVED | use: POINT (v) — "The bolt heads must be oriented toward the rear." → "MAKE SURE THAT THE BOLT HEADS POINT TO THE REAR." |
| origin (n) | NOT APPROVED | use: SOURCE (n) — "The origin of the problem is in the fuel system." → "THE SOURCE OF THE PROBLEM IS IN THE FUEL SYSTEM." |
| original (adj) | NOT APPROVED | use: INITIAL (adj) — "The slide returns to the original position." → "THE SLIDE GOES BACK TO ITS INITIAL POSITION." |
| originate (v) | NOT APPROVED | use: SOURCE (n) — "If the fuel leak originates at the valve, replace the valve seals." → "IF THE VALVE IS THE SOURCE OF THE FUEL LEAK, REPLACE THE VALVE SEALS." |
| OTHER (adj) | Not the same as that given before |  |
| OTHER (pron) | That which is not the same as that given before |  |
| otherwise (adv) | NOT APPROVED | use: DIFFERENTLY (adv) — IF …NOT — "Check that the rods are adjusted correctly, otherwise adjust them as follows: Unless the instructions tell you otherwise, do repair scheme No. 4." → "MAKE SURE THAT THE RODS ARE ADJUSTED CORRECTLY. IF THE ADJUSTMENT IS NOT CORRECT, ADJUST THEM AS FOLLOWS: UNLESS THE INSTRUCTIONS TELL YOU DIFFERENTLY, DO REPAIR SCHEME No. 4." |
| OUT (adj) | Away from, or not in, a location or position |  |
| OUT (adv) | To a position away from the inside |  |
| OUT OF (prep) | 1. Through or from the inside to the outside 2. Not in |  |
| OUTBOARD (adj) | Farther from the longitudinal axis of something |  |
| OUTBOARD (adv) | In, or to, a position farther from the longitudinal axis of something |  |
| OUTBOARD OF (prep) | At a position farther from the longitudinal axis |  |
| OUTDOORS (adv) | Not in a building |  |
| OUTER (adj) | Located on the outside or farther from the center of an object |  |
| outline (v) | NOT APPROVED | use: GIVE (v) — "This section outlines the procedures needed to find the faults." → "THIS SECTION GIVES YOU THE PROCEDURES THAT ARE NECESSARY TO FIND THE FAULTS." |
| OUTPUT (n) | The data, power, energy that comes out of equipment or a system |  |
| outside (adj) | NOT APPROVED | use: EXTERNAL (adj); OUTER (adj) |
| outside (adv) | NOT APPROVED | use: OUTDOORS (adv) — "Do this procedure outside." → "DO THIS PROCEDURE OUTDOORS." |
| outside (n) | NOT APPROVED | use: EXTERNAL (adj); OUTER (adj) |
| outside (prep) | NOT APPROVED | use: NEAR (prep) — "When you do work in a fuel tank, a second person must be outside the tank at all times." → "WHEN YOU DO WORK IN A FUEL TANK, A SECOND PERSON MUST BE NEAR THE TANK AT ALL TIMES." |
| outwards (adv) | NOT APPROVED | use: OUT (adv) — "Move the door outwards and forwards." → "MOVE THE DOOR OUT AND FORWARD." |
| over (prep) | NOT APPROVED | use: ABOVE (prep); ALONG (prep); ON (prep); MORE THAN — For movement above land or water, use a technical noun. |
| OVERBOARD (adv) | Out of a vessel |  |
| overfill (v) | NOT APPROVED | use: TOO MUCH — "Do not overfill the lubrication hole." → "DO NOT PUT TOO MUCH FLUID IN THE LUBRICATION HOLE." |
| overfull (adj) | NOT APPROVED | use: TOO FULL — "If the tank is overfull, you cannot pressurize it correctly." → "IF THE TANK IS TOO FULL, YOU CANNOT PRESSURIZE IT CORRECTLY." |
| overhaul (v) | NOT APPROVED | use: OVERHAUL (TN) — "Overhaul the No. 2 engine." → "DO AN OVERHAUL OF THE No. 2 ENGINE." |
| overheat (v) | NOT APPROVED | use: TOO HOT — "Rapid charging overheats the oxygen bottle." → "IF YOU PRESSURIZE THE OXYGEN BOTTLE QUICKLY, IT WILL BECOME TOO HOT." |
| OVERLAP (n) | The area in which a part of one surface is on a part of a second surface |  |
| overlap (v) | NOT APPROVED | use: OVERLAP (n) — "Overlap the surfaces by 10 mm." → "MAKE AN OVERLAP OF 10 mm." |
| OVERRIDE (v) | To prevent the automatic operation of a part or system | forms: OVERRIDES, OVERRODE, OVERRIDDEN |
| overtighten (v) | NOT APPROVED | use: TIGHTEN TOO MUCH; TOO TIGHT; TOO TIGHTLY |
| pack (v) | NOT APPROVED | use: PUT (v); FILL (v) |
| PAINT (v) | To apply paint to something | forms: PAINTS, PAINTED, PAINTED |
| PAIR (n) | Two objects that are the same or almost the same, and/or that you use together |  |
| PARALLEL (adj) | Along lines that stay a constant distance apart at all points |  |
| PARK (v) | To stop a vehicle and to let it stay in one position on the ground | forms: PARKS, PARKED, PARKED |
| PART (n) | 1. A constituent of an object, machine, component, assembly, or equipment 2. A piece or section of a whole |  |
| part (v) | NOT APPROVED | use: DISCONNECT (v) — "Part the pipes." → "DISCONNECT THE PIPES." |
| partial (adj) | NOT APPROVED | use: NOT FULLY — "If only partial extension of the rods occurs, do the adjustment again." → "IF THE RODS DO NOT FULLY EXTEND, ADJUST THEM AGAIN." |
| partially (adv) | NOT APPROVED | use: NOT FULLY — "If the flaps only partially extend, do the test again." → "IF THE FLAPS DO NOT FULLY EXTEND, DO THE TEST AGAIN." |
| PARTICLE (n) | A very small piece of material |  |
| particular (adj) | NOT APPROVED | use: ONLY APPLICABLE; VERY (adv) |
| particularly (adv) | NOT APPROVED | use: VERY (adv) — "This precaution is particularly important." → "THIS PRECAUTION IS VERY IMPORTANT." |
| partly (adv) | NOT APPROVED | use: NOT FULLY — "If the valve opens only partly, examine the positions of the end stops on the actuator." → "IF THE VALVE DOES NOT FULLY OPEN, EXAMINE THE POSITIONS OF THE END STOPS ON THE ACTUATOR." |
| pass (v) | NOT APPROVED | use: GO (v); THROUGH (prep); GIVE (v) |
| passage (n) | NOT APPROVED | use: FLOW (n); HOLE (n); OPENING (n) |
| past (prep) | NOT APPROVED | use: AROUND (prep); THROUGH (prep) |
| PASTE (n) | A wet, flexible mixture or compound |  |
| PATCH (n) | A piece of material that you use to repair a surface or hole |  |
| penetrate (v) | NOT APPROVED | use: GO THROUGH; GO INTO |
| people (n) | NOT APPROVED | use: PERSON (n); PERSONNEL (n); PERSONNEL (n). — To select the correct alternative, refer to the approved meanings of PERSON (n) and |
| per (prep) | NOT APPROVED | use: FOR EACH; REFER (v) |
| perforated (adj) | NOT APPROVED | use: HOLE (n) — "Make sure that the membrane is not perforated." → "MAKE SURE THAT THERE ARE NO HOLES IN THE MEMBRANE." |
| perform (v) | NOT APPROVED | use: DO (v); MEASURE (v) — You can use a more accurate verb. |
| PERFORMANCE (n) | The ability of a part, a mechanism, or system to do its necessary function when you compare it with a standard or specification | For other meanings, use: DO (v) |
| PERIOD (n) | A quantity of time |  |
| periodically (adv) | NOT APPROVED | use: INTERVAL (n) — Give the value. — "Examine the condition of hoses and seals periodically." → "EXAMINE THE CONDITION OF THE HOSES AND SEALS AT INTERVALS OF TWO YEARS." |
| PERMANENT (adj) | Without a limit in time |  |
| PERMANENTLY (adv) | In a permanent manner |  |
| permissible (adj) | NOT APPROVED | use: PERMITTED (adj) — "Equivalent materials are also permissible." → "EQUIVALENT MATERIALS ARE ALSO PERMITTED." |
| permit (v) | NOT APPROVED | use: LET (v) — "Do not permit the fluid to touch you." → "DO NOT LET THE FLUID TOUCH YOU." |
| PERMITTED (adj) | Allowed |  |
| PERPENDICULAR (adj) | At a 90 degree angle to a given line or plane |  |
| persist (v) | NOT APPROVED | use: CONTINUE (v) — "If the fault message persists, push the AUDIO CANCEL switch on the test panel." → "IF THE FAULT MESSAGE CONTINUES, PUSH THE AUDIO CANCEL SWITCH ON THE TEST PANEL." |
| persistent (adj) | NOT APPROVED | use: CONTINUOUS (adj) — "If you hear persistent background noise, find the cause." → "IF YOU HEAR CONTINUOUS BACKGROUND NOISE, FIND THE CAUSE." |
| PERSON (n) | A human being |  |
| PERSONNEL (n) | Persons employed in a group or organization |  |
| pertinent (adj) | NOT APPROVED | use: APPLICABLE (adj) — "Make sure that you have all the pertinent documents." → "MAKE SURE THAT YOU HAVE ALL THE APPLICABLE DOCUMENTS." |
| picket (v) | NOT APPROVED | use: MOOR (v) — "Picket the vehicle in strong winds." → "IF STRONG WINDS OCCUR, MOOR THE VEHICLE." |
| PIECE (n) | A quantity or segment of a whole that you can use on its own, or that can operate as an individual item |  |
| pierced (adj) | NOT APPROVED | use: HOLE (n) — "Make sure that the membrane is not pierced." → "MAKE SURE THAT THERE ARE NO HOLES IN THE MEMBRANE." |
| placard (v) | NOT APPROVED | use: PUT (v) — (A PLACARD [TN]) — "Placard the controls before you start the test." → "BEFORE YOU START THE TEST, PUT A PLACARD ON THE CONTROLS." |
| place (n) | NOT APPROVED | use: POSITION (n); AREA (n) |
| place (v) | NOT APPROVED | use: PUT (v) — "Place the manifold in position." → "PUT THE MANIFOLD IN POSITION." |
| PLAY (n) | Free movement, the length or dimension of this movement |  |
| plot (v) | NOT APPROVED | use: MAKE (v) — (A PLOT [TN]) — "Plot these points." → "MAKE A PLOT OF THESE POINTS." |
| plug (v) | NOT APPROVED | use: CONNECT (v); SEAL (v) — (WITH A PLUG [TN] OR PLUGS [TN]) |
| PLUS (prep) | With the addition of |  |
| PNEUMATIC (adj) | Related to, or operated by gas pressure |  |
| PNEUMATICALLY (adv) | With pneumatic power |  |
| POINT (n) | 1. A sharp or tapered end 2. An accurate location |  |
| POINT (v) | 1. To show the position or direction of 2. To turn something in a specified direction | forms: POINTS, POINTED, POINTED |
| POISONOUS (adj) | That contains poison |  |
| POLISH (v) | To make smooth or shiny | forms: POLISHES, POLISHED, POLISHED |
| poor (adj) | NOT APPROVED | use: UNSATISFACTORY (adj); DEFECTIVE (adj); UNSERVICEABLE (adj) |
| pop (v) | NOT APPROVED | use: OPEN (v); PROTRUDE (v); OUT (adv) |
| port (adj) | NOT APPROVED | use: LEFT (adj) — "Remove the wing tip brake from the port wing." → "REMOVE THE WING TIP BRAKE FROM THE LEFT WING." |
| portion (n) | NOT APPROVED | use: PIECE (n); PART (n) |
| POSITION (n) | The attitude or setting of something that you can adjust, or the place or site where you put something |  |
| position (v) | NOT APPROVED | use: PUT (v); SET (v) |
| POSSIBLE (adj) | That can occur |  |
| POSSIBLY (adv) | That can occur |  |
| potential (adj) | NOT APPROVED | use: POSSIBLE (adj) — "Put barriers around all the potential danger areas." → "PUT BARRIERS AROUND ALL THE POSSIBLE DANGER AREAS." |
| pour (v) | NOT APPROVED | use: PUT (v) — "Pour the mixture into the cylinder." → "PUT THE MIXTURE INTO THE CYLINDER." |
| power (v) | NOT APPROVED | use: SUPPLY (v) — "The battery powers the circuits." → "THE BATTERY SUPPLIES POWER TO THE CIRCUITS." |
| PRECAUTION (n) | That which you do to prevent injury and/or damage |  |
| precautionary (adj) | NOT APPROVED | use: PRECAUTION (n) — "Take these precautionary measures." → "OBEY THESE PRECAUTIONS." |
| precede (v) | NOT APPROVED | use: BEFORE (conj) — "Application of the tape must be preceded by cleaning of the surface." → "BEFORE YOU APPLY THE TAPE, CLEAN THE SURFACE." |
| precise (adj) | NOT APPROVED | use: ACCURATE (adj) — "The gyro requires precise adjustment." → "THE GYRO ADJUSTMENT MUST BE ACCURATE." |
| precisely (adv) | NOT APPROVED | use: ACCURATELY (adv) — "The angle of the camera must be adjusted precisely." → "ADJUST THE ANGLE OF THE CAMERA ACCURATELY." |
| PRECISION (n) | The quality of being accurate |  |
| preferable (adj) | NOT APPROVED | use: RECOMMEND (v) — "It is possible to mix approved engine oils of the same type, but. according to the Standard Practices Manual. it is always preferable to use the same type of engine oil." → "IT IS POSSIBLE TO MIX APPROVED ENGINE OILS OF THE SAME TYPE. BUT THE STANDARD PRACTICES MANUAL RECOMMENDS THAT YOU ALWAYS USE THE SAME TYPE OF ENGINE OIL." |
| preferably (adv) | NOT APPROVED | use: IF IT IS POSSIBLE — "Preferably, apply this adhesive outdoors." → "IF IT IS POSSIBLE, APPLY THIS ADHESIVE OUTDOORS." |
| preheat (v) | NOT APPROVED | use: HEAT (n) — "Preheat the area with a heat lamp." → "BEFORE YOU START THIS PROCEDURE, APPLY HEAT TO THE AREA WITH A HEAT LAMP." |
| preload (v) | NOT APPROVED | use: LOAD (TN) — "Preload the spring to 10 lb." → "BEFORE YOU START THIS PROCEDURE, APPLY A LOAD OF 10 lb TO THE SPRING." |
| premature (adj) | NOT APPROVED | use: BEFORE (conj) — "If the valve opening is premature, stop the test." → "IF THE VALVE OPENS BEFORE THE SET PRESSURE, STOP THE TEST." |
| prematurely (adv) | NOT APPROVED | use: BEFORE (conj) — "If the valve opens prematurely, stop the test." → "IF THE VALVE OPENS BEFORE THE SET PRESSURE, STOP THE TEST." |
| preparation (n) | NOT APPROVED | use: PREPARE (v) — "Mixture preparation must be accomplished 20 minutes before use." → "PREPARE THE MIXTURE 20 MINUTES BEFORE YOU USE IT." |
| PREPARE (v) | To make or become ready | forms: PREPARES, PREPARED, PREPARED |
| prescribed (adj) | NOT APPROVED | use: SPECIFIED (adj) — "Fill the container with the prescribed coolant fluid." → "FILL THE CONTAINER WITH THE SPECIFIED COOLANT FLUID." |
| presence (n) | NOT APPROVED | use: BE (v) — "This inspection is necessary in the presence of defects." → "THIS INSPECTION IS NECESSARY WHEN THERE ARE DEFECTS." |
| present (adj) | NOT APPROVED | use: BE (v) — "If a voltage is present at pin C of connector F7, the unit is faulty." → "IF THERE IS A VOLTAGE AT PIN C OF CONNECTOR F7, THE UNIT IS UNSERVICEABLE." |
| present (v) | NOT APPROVED | use: GIVE (v); SHOW (v) |
| preserve (v) | NOT APPROVED | use: PRESERVATION (TN) — "This procedure will preserve the steel cables." → "THIS PROCEDURE IS FOR THE PRESERVATION OF STEEL CABLES." |
| preset (v) | NOT APPROVED | use: SET (v) — "Preset the tension indicator to zero." → "SET THE TENSION INDICATOR TO ZERO." |
| press (v) | NOT APPROVED | use: PUSH (v) — "Press and hold the TEST button." → "PUSH AND HOLD THE TEST BUTTON." |
| PRESSURIZATION (n) | The procedure that supplies or increases the pressure |  |
| PRESSURIZE (v) | To supply pressure | forms: PRESSURIZES, PRESSURIZED, PRESSURIZED |
| PREVENT (v) | To make sure that something does not occur | forms: PREVENTS, PREVENTED, PREVENTED |
| prevent (from) (v) | NOT APPROVED | use: LET (v) — "Prevent the door from opening." → "DO NOT LET THE DOOR OPEN." |
| preventive (adj) | NOT APPROVED | use: PREVENT (v) — "This coating is a preventive measure for corrosion." → "THIS COATING PREVENTS CORROSION." |
| PREVIOUS (adj) | That goes before in an unspecified time or sequence Be accurate. Use LAST (adj) for the event that occurs immediately before in time or sequence. |  |
| PREVIOUSLY (adv) | Before, earlier, in the past |  |
| primarily (adv) | NOT APPROVED | use: PRIMARY (adj) — "The hydraulic system primarily supplies the pressure to operate the flight controls." → "THE PRIMARY FUNCTION OF THE HYDRAULIC SYSTEM IS TO SUPPLY THE PRESSURE TO OPERATE THE FLIGHT CONTROLS." |
| PRIMARY (adj) | First in importance |  |
| prime (v) | NOT APPROVED | use: FILL (v); PUT (v) |
| principal (adj) | NOT APPROVED | use: PRIMARY (adj) — "The principal function of the system is to supply electrical power to the control panel ." → "THE PRIMARY FUNCTION OF THE SYSTEM IS TO SUPPLY ELECTRICAL POWER TO THE CONTROL PANEL." |
| prior to (prep) | NOT APPROVED | use: BEFORE (conj) — "Drain the system prior to disconnecting the hoses." → "BEFORE YOU DISCONNECT THE HOSES, DRAIN THE SYSTEM." |
| priority (n) | NOT APPROVED | use: IMPORTANT (adj); BEFORE (prep); FIRST (adv) |
| probability (n) | NOT APPROVED | use: RISK (n) — "Obey the safety precautions to decrease the probability of fire." → "TO DECREASE THE RISK OF FIRE, OBEY THE SAFETY PRECAUTIONS." |
| probable (adj) | NOT APPROVED | use: VERY POSSIBLE; RISK (n) |
| probe (v) | NOT APPROVED | use: FIND (v) — (WITH A PROBE [TN]) — "Probe the tube to find the blockage." → "FIND THE BLOCKAGE IN THE TUBE WITH AN APPLICABLE PROBE." |
| PROBLEM (n) | Something that is difficult and for which you must find the correct answer |  |
| PROCEDURE (n) | Steps that are in a sequence |  |
| proceed (v) | NOT APPROVED | use: CONTINUE (v) — "Proceed with the electrical test." → "CONTINUE WITH THE ELECTRICAL TEST." |
| process (in the process of ) (prep) | NOT APPROVED | use: DURING (prep); WHILE (conj) |
| process (n) | NOT APPROVED | use: PROCEDURE (n) — This word is a technical noun when it means a sequence of changes that occur and cause a result. — "These two assembly processes are almost the same." → "THESE TWO ASSEMBLY PROCEDURES ARE ALMOST THE SAME. CORROSION IS AN ELECTROLYTIC PROCESS." |
| process (v) | NOT APPROVED | use: PROCEDURE (n) — DO (v) THE … — "Process the parts in an electrolytic bath." → "PUT THE PARTS IN AN ELECTROLYTIC BATH. THEN, DO THE ELECTROPLATING PROCEDURE." |
| produce (v) | NOT APPROVED | use: CAUSE (v); GIVE (v); MAKE (v); SUPPLY (v) |
| product (n) | NOT APPROVED | Be accurate. If it is possible, use the name of the product. — "When you clean this unit, use the correct product. This product is dangerous." → "WHEN YOU CLEAN THIS UNIT, USE THE CORRECT SOLVENT. TRICHLOROETHANE IS A DANGEROUS MATERIAL." |
| profile (n) | NOT APPROVED | use: CONTOUR (n) — "Make sure that the profile of the template is the same." → "MAKE SURE THAT THE CONTOUR OF THE TEMPLATE IS THE SAME." |
| program (n) | NOT APPROVED | use: SEQUENCE (n) — "Disassemble the rotor according to the following program:" → "DISASSEMBLE THE ROTOR IN THIS SEQUENCE:" |
| progress (n) | NOT APPROVED | use: CONTINUE (v); IN PROGRESS — Also refer to (adv). |
| progress (v) | NOT APPROVED | use: CONTINUE (v) — "You can progress with the test." → "YOU CAN CONTINUE THE TEST." |
| progressive (adj) | NOT APPROVED | use: GRADUALLY (adv) — "Apply progressive torque to the nut." → "GRADUALLY TORQUE THE NUT." |
| progressively (adv) | NOT APPROVED | use: GRADUALLY (adv) — "Torque the bolts progressively." → "TORQUE THE BOLTS GRADUALLY." |
| prohibit (v) | NOT APPROVED | use: PREVENT (v) — TELL (NOT TO) (v) — "Display a warning notice on the panel prohibiting the operation of the controls. Prohibit the use of asbestos parts." → "PUT A WARNING NOTICE ON THE PANEL TO PREVENT OPERATION OF THE CONTROLS. TELL THE PERSONNEL NOT TO USE ASBESTOS PARTS." |
| prolonged (adj) | NOT APPROVED | use: LONG (adj) — "Prolonged motor operation can cause damage." → "OPERATION OF THE MOTOR FOR LONG PERIODS CAN CAUSE DAMAGE TO IT." |
| prompt (adj) | NOT APPROVED | use: IMMEDIATELY (adv) — "Prompt action is required if you swallow solvent." → "IF YOU SWALLOW SOLVENT, DO NOT CAUSE VOMITING. GET MEDICAL AID IMMEDIATELY." |
| propagation (n) | NOT APPROVED | use: INCREASE (v) — If it is possible, give the dimensions or limits. — "Crack propagation can cause the part to break. Crack propagation can cause the rejection of the part. Crack propagation can cause the rejection of the part." → "IF THE DIMENSION OF A CRACK INCREASES, THE PART CAN BREAK. IF THE DEPTH OF A CRACK IS MORE THAN 0.2 mm, REJECT THE PART. IF A CRACK IS LARGER THAN 0.2 mm, REJECT THE PART." |
| proper (adj) | NOT APPROVED | use: CORRECT (adj) — "Check the unit for proper operation." → "DO A CHECK FOR THE CORRECT OPERATION OF THE UNIT." |
| properly (adv) | NOT APPROVED | use: CORRECTLY (adv) — "Close the doors properly." → "CLOSE THE DOORS CORRECTLY." |
| PROPERTY (n) | A characteristic or attribute of an object |  |
| PROPORTION (n) | The ratio of something to something else | For other meanings, use: RELATION (n) |
| proportional (adj) | NOT APPROVED | use: RELATION (n); PROPORTION (n) |
| proportionally (adv) | NOT APPROVED | use: RELATION (n) — "The cable tension changes proportionally with temperature." → "THE CABLE TENSION CHANGES IN RELATION TO THE TEMPERATURE." |
| protect (v) | NOT APPROVED | use: PREVENT (v); PROTECTION (n) |
| PROTECTION (n) | Something to prevent injury, damage, or failure |  |
| PROTECTIVE (adj) | That gives protection |  |
| PROTRUDE (v) | To be farther forward or out from an adjacent surface | forms: PROTRUDES PROTRUDED PROTRUDED |
| provide (v) | NOT APPROVED | use: GIVE (v); SUPPLY (v) |
| provided (that) (conj) | NOT APPROVED | use: IF (conj) — "Provided that a replacement part is available, replace the damaged shield." → "IF A REPLACEMENT PART IS AVAILABLE, REPLACE THE DAMAGED SHIELD." |
| providing (that) (conj) | NOT APPROVED | use: IF (conj) — "Providing that a new part is installed, you can continue the operation of the machine." → "IF A NEW PART IS INSTALLED, YOU CAN CONTINUE THE OPERATION OF THE MACHINE." |
| proximity (n) | NOT APPROVED | use: NEAR (prep) — "Do not do maintenance work in proximity to a running engine." → "DO NOT DO MAINTENANCE WORK NEAR AN ENGINE THAT IS IN OPERATION." |
| PULL (v) | To use a force on something to move it toward the source of the force Use this word together with a preposition or an adverb to show direction. | forms: PULLS, PULLED, PULLED |
| pump (v) | NOT APPROVED | use: REMOVE (v); MOVE (v) — (WITH A PUMP [TN]) (WITH A PUMP [TN]) |
| puncture (v) | NOT APPROVED | use: HOLE (n) — "Take care not to puncture the bladder." → "MAKE SURE THAT YOU DO NOT MAKE A HOLE IN THE BLADDER." |
| purge (v) | NOT APPROVED | use: REMOVE (v) — "Purge the system." → "REMOVE UNWANTED MATERIAL FROM THE SYSTEM." |
| purify (v) | NOT APPROVED | use: CLEAN (v) — "Purify the water." → "CLEAN THE WATER." |
| PUSH (v) | 1. To apply a force to something to move it away from the source of the force 2. To move with a force against something Use this word together with a preposition or an adverb to show direction. | forms: PUSHES, PUSHED, PUSHED |
| PUT (v) | To cause something to move or to be in a specified position or condition | forms: PUTS, PUT No other verb forms. |
| PUT ON (v) | To cover your skin or face with clothing, or other items that give protection | forms: PUTS ON, PUT ON No other verb forms. |
| qualified (adj) | NOT APPROVED | use: APPROVED (adj) — "A qualified person must do the important checks." → "AN APPROVED PERSON MUST DO THE IMPORTANT CHECKS." |
| QUALITY (n) | Condition, property, or type |  |
| QUANTITY (n) | A specified amount or number | For an amount that you can count, use NUMBER (n). |
| quarterly (adv) | NOT APPROVED | use: INTERVAL (n) — "Send reports to the authorities quarterly." → "SEND REPORTS TO THE AUTHORITIES AT INTERVALS OF THREE MONTHS." |
| questionable (adj) | NOT APPROVED | use: NOT SURE — "Reject the parts that are in a questionable condition." → "IF YOU ARE NOT SURE OF THEIR CONDITION, REJECT THE PARTS." |
| quick (adj) | NOT APPROVED | use: QUICKLY (adv) — "Make sure that there is no quick movement of the rod." → "MAKE SURE THAT THE ROD DOES NOT MOVE QUICKLY." |
| QUICKLY (adv) | In a fast manner |  |
| quit (v) | NOT APPROVED | use: GO (v); STOP (v) |
| quote (v) | NOT APPROVED | use: GIVE (v) — "The table quotes the maximum tolerance for the hole." → "THE TABLE GIVES THE MAXIMUM TOLERANCE FOR THE HOLE." |
| RADIAL (adj) | Along a radius |  |
| RADIALLY (adv) | Along a radius |  |
| RADIOACTIVE (adj) | Related to radioactivity |  |
| raise (v) | NOT APPROVED | use: LIFT (v); INCREASE (v); RETRACT (v) |
| RANDOM (adj) | Not regular |  |
| RANDOMLY (adv) | Not regularly |  |
| RANGE (n) | The limits within which something operates |  |
| rapid (adj) | NOT APPROVED | use: FAST (adj) — "Chemical agents cause rapid deterioration of painted surfaces." → "CHEMICAL AGENTS CAUSE FAST DETERIORATION OF PAINTED SURFACES." |
| rapidly (adv) | NOT APPROVED | use: QUICKLY (adv) — "Rapidly turn the handle clockwise." → "QUICKLY TURN THE HANDLE CLOCKWISE." |
| RATE (n) | A measurement of how frequently or how quickly something occurs |  |
| re- (prefix) | NOT APPROVED | In general, use the word AGAIN (adv) or BACK (adv) with the basic word to replace words that have “re-” as a prefix. |
| reach (v) | NOT APPROVED | use: GET (v); TOUCH (v); BE (v) |
| reactivate (v) | NOT APPROVED | use: ACTIVATE (v) — "Reactivate the mode." → "ACTIVATE THE MODE AGAIN." |
| READ (v) | To come to know information with the eyes or electronically | forms: READS, READ, READ |
| reading (n) | NOT APPROVED | use: INDICATION (n) — "Avoid an erroneous reading caused by exhaust from ground cart." → "MAKE SURE THAT THE EXHAUST FROM THE GROUND CART DOES NOT CAUSE AN INCORRECT INDICATION." |
| readjust (v) | NOT APPROVED | use: ADJUST (v) — "Readjust the linkage after the inspection." → "AFTER THE INSPECTION, ADJUST THE LINKAGE AGAIN." |
| ready (adj) | NOT APPROVED | use: PREPARE (v) — "Make sure that the control system is in an operational ready state." → "MAKE SURE THAT THE CONTROL SYSTEM IS PREPARED FOR OPERATION." |
| ready (v) | NOT APPROVED | use: PREPARE (v) — "Ready the removal kit for the removal of the strut." → "PREPARE THE REMOVAL KIT FOR THE REMOVAL OF THE STRUT." |
| real (adj) | NOT APPROVED | use: AGREE (v) — "Make sure that the gauge shows the real quantity of fuel that is in the tank." → "MAKE SURE THAT THE INDICATION ON THE GAUGE AGREES WITH THE QUANTITY OF FUEL THAT IS IN THE TANK." |
| REAR (adj) | Away from the person who looks or from a reference point |  |
| REAR (n) | The rear part or rear surface |  |
| rear of (prep) | NOT APPROVED | use: AFT OF; BEHIND (prep) |
| rearmost (adj) | NOT APPROVED | use: REAR (n) — "The rearmost half clamp is not removable." → "YOU CANNOT REMOVE THE HALF CLAMP NEAREST TO THE REAR." |
| REARWARD (adv) | In the direction of the rear |  |
| reason (n) | NOT APPROVED | use: CAUSE (n); BECAUSE OF (prep) |
| reassemble (v) | NOT APPROVED | use: ASSEMBLE (v) — "Reassemble the actuator." → "ASSEMBLE THE ACTUATOR AGAIN." |
| rebuild (v) | NOT APPROVED | use: ASSEMBLE (v) — "Rebuild the unit." → "ASSEMBLE THE UNIT AGAIN." |
| RECEIVE (v) | To get energy, material, or a signal from a different source | forms: RECEIVES, RECEIVED, RECEIVED |
| RECESS (n) | An indentation in a surface |  |
| recess (v) | NOT APPROVED | use: RECESS (n) — "Do not recess studs more than 5 mm. The flange is recessed into the fuselage." → "DO NOT MAKE A RECESS OF MORE THAN 5 mm FOR THE STUDS. THE FLANGE IS IN A RECESS IN THE FUSELAGE." |
| recharge (v) | NOT APPROVED | use: CHARGE (v); FILL (v); PRESSURIZE (v) |
| recheck (v) | NOT APPROVED | use: MEASURE (v); EXAMINE (v); CHECK (n) |
| reclaim (v) | NOT APPROVED | use: REPAIR (v) — "Reclaim the damaged fabric area." → "REPAIR THE DAMAGED FABRIC AREA." |
| recleat (v) | NOT APPROVED | use: ATTACH (v) — (TO A CLEAT [TN]) — "Recleat the tiedown cord." → "ATTACH THE TIEDOWN CORD TO A CLEAT." |
| reclose (v) | NOT APPROVED | use: CLOSE (v) — "Reclose the compartment after servicing." → "AFTER SERVICING, CLOSE THE COMPARTMENT AGAIN." |
| recoil (v) | NOT APPROVED | use: MOVE BACK; WIND (v); RECOIL (TN) |
| RECOMMEND (v) | To advise that which is best | forms: RECOMMENDS, RECOMMENDED, RECOMMENDED |
| recondition (v) | NOT APPROVED | use: REPAIR (v); OVERHAUL (TN) |
| reconstruction (n) | NOT APPROVED | use: REPAIR (n); REPAIR (v) |
| RECORD (v) | 1. To make notes of and keep data to use subsequently 2. To put data on a storage medium | forms: RECORDS, RECORDED, RECORDED |
| recover (v) | NOT APPROVED | use: COLLECT (v) — "Remove the nut and the bolt. Then, recover the washer." → "REMOVE THE NUT AND THE BOLT. THEN, COLLECT THE WASHER." |
| rectify (v) | NOT APPROVED | use: CORRECT (v) — "Rectify the defect before you restart the procedure." → "BEFORE YOU START THE PROCEDURE AGAIN, CORRECT THE DEFECT." |
| recur (v) | NOT APPROVED | use: OCCUR (v) — "If the symptoms recur, do a system test." → "IF THE SYMPTOMS OCCUR AGAIN, DO A SYSTEM TEST." |
| RECYCLE (v) | To put a used material through a process to make it possible to use it or its components again For other meanings, use: CYCLE (n) | forms: RECYCLES, RECYCLED, RECYCLED |
| reduce (v) | NOT APPROVED | use: DECREASE (v) — "Slowly reduce the speed." → "SLOWLY DECREASE THE SPEED." |
| REFER (v) | 1. To tell a person where to find information 2. To give information | forms: REFERS, REFERRED, REFERRED |
| reference (n) | NOT APPROVED | use: REFER (v) — "Reference is made to Chapter 20 for the standard torque values." → "REFER TO CHAPTER 20 FOR THE STANDARD TORQUE VALUES." |
| referenced (adj) | NOT APPROVED | use: SHOW (v) — "Make sure that this point is referenced on the graph." → "MAKE SURE THAT THE GRAPH SHOWS THIS POINT." |
| refill (v) | NOT APPROVED | use: FILL (v) — "Refill the container." → "FILL THE CONTAINER AGAIN." |
| refit (v) | NOT APPROVED | use: INSTALL (v); REPAIR (v) |
| reflect (v) | NOT APPROVED | use: REFLECTION (n) — "The reticle image reflects on the bottom surface of the glass." → "THE RETICLE IMAGE MAKES A REFLECTION ON THE BOTTOM SURFACE OF THE GLASS." |
| REFLECTION (n) | Something that occurs when energy comes against a surface which sends it back |  |
| REFUEL (v) | To supply with fuel | forms: REFUELS, REFUELED, REFUELED |
| register (v) | NOT APPROVED | use: SHOW (v) — "Adjust the “SET +40” control until the pointer registers +40." → "ADJUST THE “SET +40” CONTROL UNTIL THE POINTER SHOWS +40." |
| regrease (v) | NOT APPROVED | use: APPLY (v); MORE (adj) |
| REGULAR (adj) | At specified or equal intervals |  |
| REGULARLY (adv) | In a regular manner |  |
| regulate (v) | NOT APPROVED | use: CONTROL (v); ADJUST (v) |
| regulation (n) | NOT APPROVED | use: ADJUSTMENT (n); CONTROL (n); CONTROL (v) |
| reinflate (v) | NOT APPROVED | use: INFLATE (v) — "Reinflate the tire." → "INFLATE THE TIRE AGAIN." |
| reinforce (v) | NOT APPROVED | MAKE … STRONGER — "Doublers reinforce the joint." → "DOUBLERS MAKE THE JOINT STRONGER." |
| reinstall (v) | NOT APPROVED | use: INSTALL (v) — "Reinstall the cover after you adjust the unit." → "AFTER YOU ADJUST THE UNIT, INSTALL THE COVER AGAIN." |
| reinstallation (n) | NOT APPROVED | use: INSTALLATION (n) — "This reinstallation must be performed by qualified personnel." → "ONLY APPROVED PERSONNEL CAN DO THE INSTALLATION PROCEDURE." |
| REJECT (v) | To make a decision that something is unsatisfactory | forms: REJECTS, REJECTED, REJECTED |
| rejection (n) | NOT APPROVED | use: REJECT (v) — "Rejection is mandatory if the test proves the component to be defective." → "IF THE TEST IS NOT SATISFACTORY, REJECT THE COMPONENT." |
| relate (v) | NOT APPROVED | use: RELATED (adj) — "The procedures relate to the system test." → "THE PROCEDURES ARE RELATED TO THE SYSTEM TEST." |
| RELATED (adj) | That has a relation |  |
| RELATION (n) | The connection between two or more things caused by their functions, values, or conditions |  |
| relay (v) | NOT APPROVED | use: SEND (v) — "Relay the information to the engineering department." → "SEND THE INFORMATION TO THE ENGINEERING DEPARTMENT." |
| RELEASE (v) | To make free, to let go | forms: RELEASES, RELEASED, RELEASED |
| relevant (adj) | NOT APPROVED | use: RELATED (adj); THEIR (adj); ITS (adj) |
| relieve (v) | NOT APPROVED | use: RELEASE (v) — "Relieve the tension in the cable." → "RELEASE THE TENSION IN THE CABLE." |
| remain (v) | NOT APPROVED | use: STAY (v) — "The flags must remain out of view." → "THE FLAGS MUST STAY OUT OF VIEW." |
| REMAINING (adj) | That continues to stay |  |
| remnant (n) | NOT APPROVED | use: REMAINING (adj) — "Remove sealant remnants from the floor covering." → "REMOVE THE REMAINING SEALANT FROM THE FLOOR COVERING." |
| removable (adj) | NOT APPROVED | use: REMOVE (v) — "Find the removable part of the barrel." → "FIND THE PART OF THE BARREL THAT YOU CAN REMOVE." |
| REMOVAL (n) | A procedure which removes an object |  |
| REMOVE (v) | To take or move something away from its initial position | forms: REMOVES, REMOVED, REMOVED |
| render (v) | NOT APPROVED | use: MAKE (v) — "Render the system electrically safe." → "MAKE THE SYSTEM ELECTRICALLY SAFE." |
| renew (v) | NOT APPROVED | use: NEW (adj) — "Renew the adhesive tape." → "USE NEW ADHESIVE TAPE." |
| renovate (v) | NOT APPROVED | use: REPAIR (v); NEW (adj) |
| repack (v) | NOT APPROVED | use: PUT (v); FILL (v) |
| repaint (v) | NOT APPROVED | use: PAINT (v) — "Repaint all the surfaces." → "PAINT ALL THE SURFACES AGAIN." |
| REPAIR (n) | The act of repairing or the result when something is repaired |  |
| REPAIR (v) | To make an item serviceable | forms: REPAIRS, REPAIRED, REPAIRED |
| repairable (adj) | NOT APPROVED | use: REPAIR (v) — "This damage is repairable." → "IT IS POSSIBLE TO REPAIR THIS DAMAGE." |
| repeat (v) | NOT APPROVED | use: AGAIN (adv) — "Repeat steps (10) to (14)." → "DO STEPS (10) THRU (14) AGAIN." |
| repeated (adj) | NOT APPROVED | use: AGAIN AND AGAIN — "If repeated signals are heard, check the AP ENGAGE button on the flight mode panel." → "IF YOU HEAR SIGNALS AGAIN AND AGAIN, DO A CHECK OF THE “AP ENGAGE” BUTTON ON THE FLIGHT MODE PANEL." |
| repeatedly (adv) | NOT APPROVED | use: AGAIN AND AGAIN — "If voltage drops repeatedly, adjust the voltage regulator." → "IF THE VOLTAGE DECREASES AGAIN AND AGAIN, ADJUST THE VOLTAGE REGULATOR." |
| REPLACE (v) | To remove an item and to install a new or serviceable item of the same type | forms: REPLACES, REPLACED, REPLACED |
| REPLACEMENT (n) | The item you install when you replace an item |  |
| replenish (v) | NOT APPROVED | use: FILL (v); ADD (v); REFUEL (v) |
| REPORT (n) | The information that is recorded about a subject or occurrence |  |
| reposition (v) | NOT APPROVED | use: MOVE (v); PUT (v); SET (v) |
| represent (v) | NOT APPROVED | use: SHOW (v) — "The suction is represented by an altimeter reading." → "THE SUCTION SHOWS AS AN ALTIMETER INDICATION." |
| repressurize (v) | NOT APPROVED | use: PRESSURIZE (v) — "Repressurize the tank." → "PRESSURIZE THE TANK AGAIN." |
| request (n) | NOT APPROVED | use: TELL (v); WRITE (v) |
| request (v) | NOT APPROVED | use: TELL (v); WRITE (v) |
| require (v) | NOT APPROVED | use: NECESSARY (adj) — "During this procedure, clean filters are required." → "DURING THIS PROCEDURE, CLEAN FILTERS ARE NECESSARY." |
| reseal (v) | NOT APPROVED | use: SEAL (v) — "Reseal the container." → "SEAL THE CONTAINER AGAIN." |
| reset (v) | NOT APPROVED | use: SET (v) — "Reset the indicator to a new position." → "SET THE INDICATOR TO A NEW POSITION." |
| residual (adj) | NOT APPROVED | use: REMAINING (adj) — "Remove all residual grease." → "REMOVE ALL THE REMAINING GREASE." |
| residue (n) | NOT APPROVED | use: REMAINING (adj) — "Remove the grease residues." → "REMOVE THE REMAINING GREASE." |
| RESISTANT (adj) | That will help to prevent something |  |
| respective (adj) | NOT APPROVED | use: RELATED (adj); CORRECT (adj) |
| respectively (adv) | NOT APPROVED | use: RELATED (adj) — "Engines 1 and 2 supply the left and right wings respectively with hot air." → "ENGINES 1 AND 2 SUPPLY HOT AIR TO THEIR RELATED WINGS." |
| respond (v) | NOT APPROVED | use: RESULT (n) — "If the instrument fails to respond, do a test." → "IF THE INSTRUMENT DOES NOT GIVE A RESULT, DO A TEST." |
| rest (n) | NOT APPROVED | use: REMAINING (adj) — "The rest of these instructions only apply to approved personnel." → "THE REMAINING INSTRUCTIONS ARE APPLICABLE ONLY TO APPROVED PERSONNEL." |
| rest (v) | NOT APPROVED | use: BE (v); PUT (v) |
| restart (v) | NOT APPROVED | use: START (v) — "Restart the unit." → "START THE UNIT AGAIN." |
| restore (v) | NOT APPROVED | use: REPAIR (v); PUT (v) |
| restrain (v) | NOT APPROVED | use: HOLD (v); STOP (v); PREVENT (v); LIMIT (n) |
| restrict (v) | NOT APPROVED | use: DECREASE (v); PREVENT (v); ONLY (adv); LIMIT (n) |
| RESULT (n) | Something that occurs when you do something |  |
| result (v) | NOT APPROVED | use: CAUSE (v); RESULT (n) |
| resume (v) | NOT APPROVED | use: START (v); CONTINUE (v) |
| retain (v) | NOT APPROVED | use: KEEP (v) — "Retain the plug." → "KEEP THE PLUG." |
| retorque (v) | NOT APPROVED | use: TORQUE (v) — "Retorque the fitting." → "TORQUE THE FITTING AGAIN." |
| retouch (v) | NOT APPROVED | use: APPLY (v); PAINT (v) |
| RETRACT (v) | 1. To pull in(to) 2. To move in(to) | forms: RETRACTS, RETRACTED, RETRACTED |
| retractable (adj) | NOT APPROVED | use: RETRACT (v) — "The aircraft has a retractable landing gear." → "THE AIRCRAFT HAS A LANDING GEAR THAT RETRACTS." |
| RETRACTION (n) | The result when something retracts |  |
| return (n) | NOT APPROVED | use: GO (v) — "After the return of the ailerons to neutral, check that they are flush with the flaps." → "AFTER THE AILERONS GO BACK TO NEUTRAL, MAKE SURE THAT THEY ARE FLUSH WITH THE FLAPS." |
| return (v) | NOT APPROVED | use: GO (v) — "Plungers must return to the closed position." → "THE PLUNGERS MUST GO BACK TO THE CLOSED POSITION." |
| reusable (adj) | NOT APPROVED | use: USE (v) — "The mixture is reusable." → "YOU CAN USE THE MIXTURE AGAIN." |
| reuse (v) | NOT APPROVED | use: USE (v) — "Reuse the fabric if it is not damaged." → "IF THE FABRIC IS NOT DAMAGED, USE IT AGAIN." |
| reveal (v) | NOT APPROVED | use: SHOW (v) — "If the fuel sample reveals free water, drain the system." → "IF THE FUEL SAMPLE SHOWS FREE WATER, DRAIN THE SYSTEM." |
| reverse (adj) | NOT APPROVED | use: OPPOSITE (adj) — This word is part of a technical noun when it refers to rearward thrust. — "Move the control in the reverse direction." → "MOVE THE CONTROL IN THE OPPOSITE DIRECTION. MANUALLY TURN THE PROPELLER BLADES TO THE FULL REVERSE POSITION." |
| reverse (v) | NOT APPROVED | use: OPPOSITE (adj) — "Reverse the movement of the rod." → "MOVE THE ROD IN THE OPPOSITE DIRECTION." |
| review (n) | NOT APPROVED | use: INSPECTION (n); EXAMINE (v) |
| rewind (v) | NOT APPROVED | use: WIND (v) — "Rewind the cable onto its reel." → "WIND THE CABLE BACK ONTO ITS REEL." |
| rework (v) | NOT APPROVED | Refer to technical verbs, manufacturing processes. — "Examine for scratches and rework all damaged areas." → "EXAMINE FOR SCRATCHES. THEN, LIGHTLY POLISH ALL DAMAGED AREAS." |
| rig (v) | NOT APPROVED | use: ADJUST (v) — "Rig the system." → "ADJUST THE SYSTEM." |
| RIGHT (adj) | On the east side when you look north |  |
| right-hand (adj) | NOT APPROVED | use: RIGHT (adj) — "The fuel connector is in the right-hand wing." → "THE FUEL CONNECTOR IS IN THE RIGHT WING." |
| RIGID (adj) | That cannot easily bend or change shape |  |
| rinse (v) | NOT APPROVED | use: FLUSH (v); REMOVE (v); CLEAN (v) |
| ripped (adj) | NOT APPROVED | use: DAMAGED (adj) — "If the seat cover is ripped, replace it." → "IF THE SEAT COVER IS DAMAGED, REPLACE IT." |
| rise (n) | NOT APPROVED | use: INCREASE (v) — "When a fire starts, the temperature rise causes the detector to operate." → "WHEN A FIRE STARTS, THE TEMPERATURE INCREASES AND CAUSES THE DETECTOR TO OPERATE." |
| rise (v) | NOT APPROVED | use: INCREASE (v) — "Fill the strut with fuel until the pressure rises." → "FILL THE STRUT WITH FLUID UNTIL THE PRESSURE INCREASES." |
| RISK (n) | The possibility that something that is dangerous occurs |  |
| rope off (v) | NOT APPROVED | use: ROPE (TN) — "Rope off the area." → "PUT ROPES AROUND THE AREA." |
| rotary (adj) | NOT APPROVED | use: TURN (v) — "Use a rotary movement to align the gears." → "TURN THE GEARS TO ALIGN THEM." |
| rotate (v) | NOT APPROVED | use: TURN (v) — "Slowly rotate the vane." → "SLOWLY TURN THE VANE." |
| rotation (n) | NOT APPROVED | use: TURN (v) — "Ensure the free rotation of the fan." → "MAKE SURE THAT THE FAN TURNS FREELY." |
| rotational (adj) | NOT APPROVED | use: TURN (v) — "Use a rotational movement to align the gears." → "TURN THE GEARS TO ALIGN THEM." |
| ROUGH (adj) | Not smooth | forms: (ROUGHER, ROUGHEST) |
| roughen (v) | NOT APPROVED | use: ROUGH (adj) — "Roughen the faying surfaces." → "MAKE THE FAYING SURFACES ROUGH." |
| roughness (n) | NOT APPROVED | use: ROUGH (adj) — "Make sure the area of the bond has sufficient roughness." → "MAKE SURE THAT THE AREA OF THE BOND IS SUFFICIENTLY ROUGH." |
| round (adj) | NOT APPROVED | use: CIRCULAR (adj) — "Repair the damage with a round patch." → "REPAIR THE DAMAGE WITH A CIRCULAR PATCH." |
| ROUNDED (adj) | Not angular |  |
| route (n) | NOT APPROVED | use: ROUTING (n) — "Make sure you do not change the wire routes." → "MAKE SURE THAT YOU DO NOT CHANGE THE WIRE ROUTING." |
| route (v) | NOT APPROVED | use: PUT (v); ROUTING (n) |
| routine (adj) | NOT APPROVED | use: USUAL (adj) — "If such failures become routine, replace the unit." → "IF SUCH FAILURES BECOME USUAL, REPLACE THE UNIT." |
| ROUTING (n) | The specified direction that cables, pipes, wires, and other parts of a system must go along |  |
| ROW (n) | A number of objects in a line |  |
| RUB (v) | To move or cause something to move with pressure and friction along a surface | forms: RUBS, RUBBED, RUBBED |
| run (v) | NOT APPROVED | use: OPERATE (v) — "Run the engine at 100% thrust." → "OPERATE THE ENGINE AT 100% THRUST." |
| running (adj) | NOT APPROVED | use: FLUSH (v) — "Clean the pipes with running water." → "FLUSH THE PIPES WITH WATER." |
| SAFE (adj) | Not dangerous, disarmed | forms: (SAFER, SAFEST) |
| SAFELY (adv) | In a safe manner |  |
| SAFETY (n) | A condition that is safe |  |
| SAFETY (v) | 1. To prevent accidental operation 2. To make sure that something does not become loose | forms: SAFETIES, SAFETIED, SAFETIED |
| safety-clip (v) | NOT APPROVED | use: LOCK (v); SAFETY (v) — (WITH A CLIP [TN] OR CLIPS [TN]) (WITH A CLIP [TN] OR CLIPS [TN]) |
| safety-wire (v) | NOT APPROVED | use: LOCK (v); SAFETY (v) — (WITH LOCKWIRE [TN]) (WITH SAFETY WIRE [TN]) |
| SAME (adj) | Agrees in all details |  |
| SAME (pron) | Agrees in all details |  |
| SAMPLE (n) | A piece or quantity of something that you use for an inspection or test procedure to show that it has specified qualities |  |
| sample (v) | NOT APPROVED | use: SAMPLE (n) — "Sample and test the fuel for water contamination." → "GET A SAMPLE OF FUEL. THEN, DO A TEST FOR WATER CONTAMINATION." |
| SATISFACTORILY (adv) | In a satisfactory manner |  |
| SATISFACTORY (adj) | Agrees with all that is necessary |  |
| saturate (v) | NOT APPROVED | use: SOAK (v) — "Saturate the element for four hours." → "SOAK THE ELEMENT FOR FOUR HOURS." |
| save (v) | NOT APPROVED | use: KEEP (v) — "Save the O-rings for the subsequent procedures." → "KEEP THE O-RINGS FOR THE SUBSEQUENT PROCEDURES." |
| scan (v) | NOT APPROVED | use: EXAMINE (v); SCAN (TN) |
| SCHEDULE (v) | To plan something in a time or a sequence | forms: SCHEDULES, SCHEDULED, SCHEDULED |
| scored (adj) | NOT APPROVED | use: SCORE (TN) — "If the bearing race is scored, replace it." → "IF THE BEARING RACE HAS SCORES, REPLACE IT." |
| scrap (v) | NOT APPROVED | use: DISCARD (v) — "Scrap the removed seal." → "DISCARD THE REMOVED SEAL." |
| scrape (v) | NOT APPROVED | use: REMOVE (v) — (WITH A SCRAPER [TN]) — "Scrape off the old sealant." → "REMOVE THE REMAINING SEALANT WITH AN APPLICABLE SCRAPER." |
| scratched (adj) | NOT APPROVED | use: SCRATCH (TN) — "Repair the scratched surfaces." → "REPAIR THE SURFACES THAT HAVE SCRATCHES." |
| screw (v) | NOT APPROVED | use: TURN (v); ATTACH (v) — (WITH A SCREW [TN] OR SCREWS [TN]) |
| scrub (v) | NOT APPROVED | use: CLEAN (v) — (WITH A BRUSH [TN]) — "Scrub all metal parts." → "CLEAN THE METAL PARTS WITH A BRUSH." |
| SEAL (n) | Something that prevents access or leaks |  |
| SEAL (v) | To prevent access or leaks | forms: SEALS, SEALED, SEALED |
| search (v) | NOT APPROVED | use: EXAMINE (v) — "Search the surface for cracks." → "EXAMINE THE SURFACE FOR CRACKS." |
| seat (v) | NOT APPROVED | use: INSTALL (v); AGAINST (prep) |
| SECONDARY (adj) | Second in importance |  |
| secure (adj) | NOT APPROVED | use: TIGHT (adj); SAFE (adj); CORRECTLY (adv) |
| secure (v) | NOT APPROVED | use: ATTACH (v); SAFETY (v) |
| securely (adv) | NOT APPROVED | use: CORRECTLY (adv); SAFELY (adv); TIGHT (adj) |
| security (n) | NOT APPROVED | use: CORRECTLY (adv) — "Check the security of the components." → "MAKE SURE THAT THE COMPONENTS ARE CORRECTLY ATTACHED." |
| SEE (v) | To know with the eyes | For other meanings, use: REFER (v); EXAMINE (v); MAKE SURE (v); forms: SEES, SAW, SEEN |
| seek (v) | NOT APPROVED | use: GET (v) — "Seek medical attention immediately." → "GET MEDICAL AID IMMEDIATELY." |
| seepage (n) | NOT APPROVED | use: LEAKAGE (n) — "Clean the areas where there is hydraulic fluid seepage." → "CLEAN THE AREAS WHERE THERE IS HYDRAULIC FLUID LEAKAGE." |
| seized (adj) | NOT APPROVED | use: CATCH (v); MOVE (v); TURN (v) |
| SELECT (v) | To make a choice | Do not use this word as a synonym for SET (v).; forms: SELECTS, SELECTED, SELECTED |
| SELECTION (n) | The action or result of choosing |  |
| SEMICIRCULAR (adj) | That has the shape of half a circle |  |
| SEND (v) | To cause to go | forms: SENDS, SENT, SENT |
| SENSE (v) | To get an input automatically | forms: SENSES, SENSED, SENSED |
| SENSITIVE (adj) | That can sense small changes |  |
| separable (adj) | NOT APPROVED | use: DISASSEMBLE (v); DISCONNECT (v) |
| separate (adj) | NOT APPROVED | use: ISOLATED (adj); DIFFERENT (adj); NOT CONNECTED; NOT ATTACHED |
| separate (v) | NOT APPROVED | use: DISCONNECT (v); DIVIDE (v) |
| separately (adv) | NOT APPROVED | use: INDEPENDENTLY (adv) — "The system monitors the condition of the parts separately." → "THE SYSTEM MONITORS THE CONDITION OF THE PARTS INDEPENDENTLY." |
| SEPARATION (n) | The action or result of separating |  |
| SEQUENCE (n) | The relation of items that follow one after the other in a list or the relation of steps or events that occur one after the other in time |  |
| serious (adj) | NOT APPROVED | use: IMPORTANT (adj); DANGEROUS (adj) |
| serrated (adj) | NOT APPROVED | use: SERRATION (n) — "Use gloves when handling parts with serrated edges." → "USE GLOVES WHEN YOU TOUCH PARTS WITH EDGE SERRATIONS." |
| SERRATION (n) | One or more notches or teeth as in a saw |  |
| serve (v) | NOT APPROVED | Use an accurate verb. — "The radio master switch serves to control the bus bar." → "THE RADIO MASTER SWITCH CONTROLS THE BUS BAR." |
| service (v) | NOT APPROVED | use: SERVICING (n) — "Service the fire extinguishers." → "DO THE SERVICING OF THE FIRE EXTINGUISHERS." |
| serviceability (n) | NOT APPROVED | use: SERVICEABLE (adj) — "The serviceability of the tire is not affected by any cut smaller than 10 mm." → "THE TIRE IS SERVICEABLE IF THE CUTS ARE SMALLER THAN 10 mm." |
| SERVICEABLE (adj) | Correct or satisfactory |  |
| SERVICING (n) | The steps necessary to prepare something for operation |  |
| SET (n) | A group of related items that you (can) use for the same purpose |  |
| SET (v) | To put something into a given adjustment, condition, or mode | forms: SETS, SET, SET |
| setting (n) | NOT APPROVED | use: ADJUSTMENT (n); POSITION (n); SET (v) |
| settle (v) | NOT APPROVED | use: COLLECT (v); STABLE (adj) |
| sever (v) | NOT APPROVED | use: CUT (v) — "Make sure you do not sever the control cable." → "MAKE SURE THAT YOU DO NOT CUT THE CONTROL CABLE." |
| several (adj) | NOT APPROVED | use: SOME (adj) — If this alternative is not sufficient, give the range, quantity, number, or minimum value. — "Several functions are not available. Soak the filler caps in distilled water for several hours." → "SOME FUNCTIONS ARE NOT AVAILABLE. SOAK THE FILLER CAPS IN DISTILLED WATER FOR A MINIMUM OF EIGHT HOURS." |
| severe (adj) | NOT APPROVED | use: DANGEROUS (adj) — "This antiseptic can cause severe skin problems." → "THIS ANTISEPTIC CAN BE DANGEROUS FOR YOUR SKIN." |
| SHAKE (v) | To move or cause to move quickly up and down or from side to side | forms: SHAKES, SHOOK, SHAKEN |
| shall (v) | NOT APPROVED | use: MUST (v) — "Holes shall not have sharp edges." → "HOLES MUST NOT HAVE SHARP EDGES." |
| SHAPE (n) | The contour of an object |  |
| shape (v) | NOT APPROVED | use: SHAPE (n) — "Shape the patch to suit the cutout." → "MAKE THE PATCH THE SAME SHAPE AS THE CUTOUT." |
| SHARP (adj) | That can cut or make a hole | forms: (SHARPER, SHARPEST) |
| sharply (adv) | NOT APPROVED | use: QUICKLY (adv); SUDDENLY (adv) |
| shear (v) | NOT APPROVED | use: BREAK (v); CUT (v) |
| SHEET (n) | A piece of material that is thin in relation to its length and width |  |
| shield (v) | NOT APPROVED | use: PREVENT (v); PROTECTION (n) |
| shift (v) | NOT APPROVED | use: MOVE (v) — "Shift the lever forward." → "MOVE THE LEVER FORWARD." |
| SHINY (adj) | That can cause a reflection of light | forms: (SHINIER, SHINIEST) |
| SHOCK (n) | The sudden effect of energy on a person or object |  |
| SHORT (adj) | That has small length or duration If it is possible, be accurate. | forms: (SHORTER, SHORTEST) |
| shorten (v) | NOT APPROVED | use: DECREASE (v) — "Do not shorten the sterilization time." → "DO NOT DECREASE THE STERILIZATION TIME." |
| should (v) | NOT APPROVED | use: MUST (v); IF (conj) |
| SHOW (v) | 1. To cause to be seen 2. To be in view or come into view | forms: SHOWS, SHOWED, SHOWN |
| shut down (v) | NOT APPROVED | use: STOP (v) — "Shut down the engine." → "STOP THE ENGINE." |
| SIDE (n) | 1. The specified surface or area of an object 2. A location or direction that has a relationship to a center or a line of division |  |
| sideways (adv) | NOT APPROVED | use: SIDE (n) — "Push the unit out and then move it sideways." → "PUSH THE UNIT OUT AND THEN MOVE IT TO THE LEFT SIDE." |
| sight (n) | NOT APPROVED | use: VIEW (n) — "Turn the knob to make the display go out of sight." → "TURN THE KNOB TO MAKE THE DISPLAY GO OUT OF VIEW." |
| sight (v) | NOT APPROVED | use: LOOK (v) — "Sight along the skin." → "LOOK ALONG THE SKIN." |
| SIGN (n) | The indication of a possible condition |  |
| significant (adj) | NOT APPROVED | use: IMPORTANT (adj) — "This procedure is significant for the correct operation of the unit." → "THIS PROCEDURE IS IMPORTANT FOR THE CORRECT OPERATION OF THE UNIT." |
| silence (v) | NOT APPROVED | use: STOP (v) — "Silence the alarm bell." → "STOP THE ALARM BELL." |
| similar (adj) | NOT APPROVED | use: EQUIVALENT (adj); ALMOST THE SAME |
| SIMULATE (v) | To make a condition that is the same as one that can occur in operation | forms: SIMULATES, SIMULATED, SIMULATED |
| simultaneous (adj) | NOT APPROVED | use: AT THE SAME TIME — "Simultaneous removal of the filter element and the filter housing is obligatory." → "REMOVE THE FILTER ELEMENT AND THE FILTER HOUSING AT THE SAME TIME." |
| simultaneously (adv) | NOT APPROVED | use: AT THE SAME TIME — "Do these two steps simultaneously." → "DO THESE TWO STEPS AT THE SAME TIME." |
| SINCE (conj) | Function word that shows: “from some time in the past until a later time or now” | For other meanings, use: BECAUSE (conj) |
| situated (adj) | NOT APPROVED | use: INSTALL (v); BE (v) |
| situation (n) | NOT APPROVED | use: CONDITION (n) — Use the plural form. — "The algorithm adapts to the new situation." → "THE ALGORITHM ADAPTS TO THE NEW CONDITIONS." |
| size (n) | NOT APPROVED | use: DIMENSION (n) — "These parts are of different sizes." → "THESE PARTS HAVE DIFFERENT DIMENSIONS." |
| skid (v) | NOT APPROVED | use: SKID (TN) — "This indicator indicates that the car is skidding." → "THIS INDICATOR SHOWS THAT THE CAR IS IN A SKID." |
| slack (adj) | NOT APPROVED | use: TENSION (TN) — "Check for slack control cables." → "MAKE SURE THAT THE TENSION IN THE CONTROL CABLES IS CORRECT." |
| slack (n) | NOT APPROVED | use: TENSION (TN) — "Check for slack in the control cables." → "MAKE SURE THAT THE TENSION IN THE CONTROL CABLES IS CORRECT." |
| slacken (v) | NOT APPROVED | use: TENSION (TN) — "Slacken the control cables." → "RELEASE THE TENSION IN THE CONTROL CABLES." |
| slackness (n) | NOT APPROVED | use: TENSION (TN) — "Make sure there is no slackness in the cables." → "MAKE SURE THAT THE TENSION IN THE CABLES IS CORRECT." |
| slave (v) | NOT APPROVED | use: CONTROL (v) — "The copilot's indicators are slaved to the pilot's indicators." → "THE PILOT'S INDICATORS CONTROL THE COPILOT'S INDICATORS." |
| slide (v) | NOT APPROVED | use: MOVE (v) — "Slide the computer horizontally to avoid damage." → "MOVE THE COMPUTER HORIZONTALLY TO PREVENT DAMAGE." |
| slight (adj) | NOT APPROVED | use: SMALL (adj); LIGHT (adj) |
| slightly (adv) | NOT APPROVED | use: SMALL (adj) — "Move the adapter slightly forward." → "MOVE THE ADAPTER A SMALL DISTANCE FORWARD." |
| SLOPE (n) | A surface that is not level |  |
| SLOT (n) | A long opening that is not wide |  |
| SLOW (adj) | At low speed | forms: (SLOWER, SLOWEST) |
| slow down (v) | NOT APPROVED | use: DECREASE (v) — "Slow down the screwing machine to prevent damage to fasteners." → "DECREASE THE SPEED OF THE SCREWING MACHINE TO PREVENT DAMAGE TO FASTENERS." |
| SLOWLY (adv) | In a slow manner |  |
| sluggish (adj) | NOT APPROVED | use: SLOW (adj) — "If the movement of the needle is sluggish, replace the sensor." → "IF THE MOVEMENT OF THE NEEDLE IS TOO SLOW, REPLACE THE SENSOR." |
| SMALL (adj) | Less than average in dimension, quantity, quality, or capacity | forms: (SMALLER, SMALLEST) |
| smear (v) | NOT APPROVED | use: APPLY (v) — "Smear grease on the taper sleeve." → "APPLY GREASE TO THE TAPER SLEEVE." |
| SMELL (v) | To sense with the nose | forms: SMELLS, SMELLED, SMELLED |
| SMOKE (n) | A gas that has particles of burned material and that you can see |  |
| SMOKE (v) | To breathe the fumes of burning material and especially tobacco | forms: SMOKES, SMOKED, SMOKED |
| SMOOTH (adj) | 1. That has a continuous uniform surface 2. That has a constant rate of movement | forms: (SMOOTHER, SMOOTHEST) |
| smooth (v) | NOT APPROVED | use: SMOOTH (adj) — "Smooth the tape out." → "MAKE THE TAPE SMOOTH." |
| SMOOTHLY (adv) | In a smooth manner |  |
| snag (v) | NOT APPROVED | use: CATCH (v) — "The cloth will snag on broken wires." → "THE CLOTH WILL CATCH ON BROKEN WIRES." |
| snap (n) | NOT APPROVED | use: CLICK (n) — "Ensure that there is a snap when you fit the spring clip." → "WHEN YOU ATTACH THE SPRING CLIP, MAKE SURE THAT YOU HEAR A CLICK." |
| snap (v) | NOT APPROVED | use: MOVE QUICKLY; BREAK (v) |
| so (that) (conj) | NOT APPROVED | use: UNTIL (prep); PREVENT (v) |
| SOAK (v) | 1. To put something into a liquid and keep it there until it is fully wet or soft 2. To stay in liquid until fully wet or soft. | forms: SOAKS, SOAKED, SOAKED |
| soapy (adj) | NOT APPROVED | use: SOAP (TN) — "Clean the surface using soapy water." → "CLEAN THE SURFACE WITH A SOLUTION OF SOAP AND WATER." |
| SOFT (adj) | Flexible, not hard | forms: (SOFTER, SOFTEST) |
| soften (v) | NOT APPROVED | MAKE…SOFT — "Put the material into the solvent to soften the compound." → "PUT THE MATERIAL INTO THE SOLVENT TO MAKE THE COMPOUND SOFT." |
| soiled (adj) | NOT APPROVED | use: DIRTY (adj) — "Scrap the soiled rags." → "DISCARD THE DIRTY RAGS." |
| SOLID (adj) | That has the properties of a solid |  |
| SOLID (n) | Material that is not a gas or a liquid |  |
| solidify (v) | NOT APPROVED | use: SOLID (adj) — "Do not allow the foam to solidify." → "DO NOT LET THE FOAM BECOME SOLID." |
| SOLUTION (n) | 1. A liquid that includes a dissolved material 2. The answer to a problem |  |
| solve (v) | NOT APPROVED | use: SOLUTION (n) — "If the removal of the valve did not solve the problem, replace the unit." → "IF THE REMOVAL OF THE VALVE WAS NOT THE SOLUTION TO THE PROBLEM, REPLACE THE UNIT." |
| SOME (adj) | Related to a quantity not specified |  |
| SOME (pron) | Related to a quantity not specified |  |
| SOMETHING (pron) | A thing that is not determined or specified |  |
| soon (adv) | NOT APPROVED | use: TIME (n) — If it is possible, give the time. — "When you stop the power supply, the temperature will decrease soon. When you stop the power supply, the temperature will decrease soon." → "WHEN YOU STOP THE POWER SUPPLY, THE TEMPERATURE WILL DECREASE IN A SHORT TIME. WHEN YOU STOP THE POWER SUPPLY, THE TEMPERATURE WILL DECREASE IN APPROXIMATELY 1 MINUTE." |
| SOUND (n) | Something that you can hear |  |
| sound (v) | NOT APPROVED | use: OPERATE (v) — "The alarm bell sounds." → "THE ALARM BELL OPERATES." |
| SOURCE (n) | 1. Something that supplies energy or data 2. The point where something starts |  |
| SPACE (n) | A distance, area, or volume |  |
| space (v) | NOT APPROVED | use: DISTANCE (n) — "Make sure you space the holes equally." → "MAKE SURE THAT THERE IS AN EQUAL DISTANCE BETWEEN THE HOLES." |
| spacing (n) | NOT APPROVED | use: DISTANCE (n) — "The rivet spacing is given in Fig. 401." → "REFER TO FIG. 401 FOR THE DISTANCE BETWEEN RIVETS." |
| spanwise (adj) | NOT APPROVED | use: SPAN (TN) — "Check for signs of spanwise movement." → "MAKE SURE THAT THERE ARE NO SIGNS OF MOVEMENT ALONG THE SPAN." |
| sparingly (adv) | NOT APPROVED | use: QUANTITY (n) — "Apply grease sparingly." → "APPLY A SMALL QUANTITY OF GREASE." |
| SPARK (n) | A hot, bright particle of a material that burns |  |
| spark (v) | NOT APPROVED | use: SPARK (n) — "Wear goggles when using electrical equipment that sparks." → "WHEN YOU USE ELECTRICAL EQUIPMENT THAT MAKES SPARKS, USE GOGGLES." |
| SPEAK (v) | To use a voice to make words | forms: SPEAKS, SPOKE, SPOKEN |
| SPECIAL (adj) | For a specified function |  |
| SPECIALLY (adv) | In a special manner |  |
| specific (adj) | NOT APPROVED | use: APPROVED (adj); SPECIFIED (adj) |
| specifically (adv) | NOT APPROVED | use: SPECIALLY (adv) — "These materials are specifically designed for plastic surfaces." → "THESE MATERIALS ARE SPECIALLY MADE FOR PLASTIC SURFACES." |
| SPECIFIED (adj) | Given in, identified in, or related to a specification, regulation, or procedure |  |
| speck (n) | NOT APPROVED | use: PARTICLE (n) — "Remove all specks of dust from the lens." → "REMOVE ALL PARTICLES OF DUST FROM THE LENS." |
| speech (n) | NOT APPROVED | use: VOICE (n) — "If the speech is not audible, replace the unit." → "IF YOU CANNOT HEAR THE VOICE, REPLACE THE UNIT." |
| SPEED (n) | The rate of movement |  |
| SPHERICAL (adj) | That has the shape of a sphere |  |
| SPILL (v) | To accidentally flow, or cause to flow, out of a container | forms: SPILLS, SPILLED, SPILLED |
| spillage (n) | NOT APPROVED | use: CONTAMINATION (n); SPILL (v) |
| spin (v) | NOT APPROVED | TURN … QUICKLY — "Spin the wheel by hand." → "TURN THE WHEEL QUICKLY WITH YOUR HAND." |
| splash (v) | NOT APPROVED | use: GET (v) — "If fluid splashes into eyes, get medical aid." → "IF YOU GET FLUID IN YOUR EYES, GET MEDICAL AID." |
| splined (adj) | NOT APPROVED | use: SPLINE (TN) — "The drive shaft is splined." → "THE DRIVE SHAFT HAS SPLINES." |
| split (adj) | NOT APPROVED | use: DAMAGED (adj) — "Split covers must be replaced." → "REPLACE DAMAGED COVERS." |
| split (v) | NOT APPROVED | use: DIVIDE (v); BREAK (v) |
| spot (n) | NOT APPROVED | use: MARK (n); STAIN (TN) |
| spot (v) | NOT APPROVED | use: FIND (v) — "If you spot corrosion in this area, use repair scheme No. 3." → "IF YOU FIND CORROSION IN THIS AREA, USE REPAIR SCHEME No. 3." |
| SPRAY (n) | A jet of very small drops of liquid |  |
| SPRAY (v) | To apply as a spray | forms: SPRAYS, SPRAYED, SPRAYED |
| spread (v) | NOT APPROVED | use: APPLY (v) — "Spread compound evenly." → "APPLY THE COMPOUND EQUALLY." |
| spring (v) | NOT APPROVED | use: MOVE (v) — "Make certain that the pins do not spring out of the notch." → "MAKE SURE THAT THE PINS DO NOT MOVE OUT OF THE NOTCH." |
| spurious (adj) | NOT APPROVED | use: UNWANTED (adj) — "In the event of spurious indications, do a test" → "IF THERE ARE UNWANTED INDICATIONS, DO A TEST." |
| stability (n) | NOT APPROVED | use: STABLE (adj) — "Before jacking up the vehicle, make sure that its stability is ensured." → "BEFORE YOU LIFT THE VEHICLE WITH JACKS, MAKE SURE THAT IT IS STABLE." |
| stabilization (n) | NOT APPROVED | use: STABLE (adj) — "Check that oil pressure drops after stabilization of temperature." → "WHEN THE TEMPERATURE IS STABLE, MAKE SURE THAT THE OIL PRESSURE DECREASES." |
| stabilize (v) | NOT APPROVED | use: STABLE (adj) — "Allow V-bars to stabilize." → "LET THE V-BARS BECOME STABLE." |
| STABLE (adj) | That does not change or move |  |
| stage (n) | NOT APPROVED | use: STEP (n) — "Do not remove the pin at this stage." → "DURING THIS STEP, DO NOT REMOVE THE PIN." |
| stained (adj) | NOT APPROVED | use: DIRTY (adj); STAIN (TN) |
| stamp (v) | NOT APPROVED | use: PUT (v); IDENTIFY (v) — (WITH A STAMP [TN] OR STAMPS [TN]) (WITH A STAMP [TN] OR STAMPS [TN]) |
| stand (v) | NOT APPROVED | use: STAY (v) — "Do not stand near moving surfaces." → "STAY AWAY FROM SURFACES THAT MOVE." |
| STANDARD (adj) | Related to equipment and procedures that are normally used |  |
| starboard (adj) | NOT APPROVED | use: RIGHT (adj) — "On the starboard wing, move the ailerons up." → "ON THE RIGHT WING, MOVE THE AILERONS UP." |
| START (n) | The beginning of a movement or operation |  |
| START (v) | 1. To begin a procedure, movement, or operation 2. To come into being, activity, or operation | forms: STARTS, STARTED, STARTED |
| state (n) | NOT APPROVED | use: CONDITION (n) — "Examine the state of the unit." → "EXAMINE THE CONDITION OF THE UNIT." |
| state (v) | NOT APPROVED | use: TELL (v) — "Unless otherwise stated by the manufacturer, do the following procedure." → "UNLESS THE MANUFACTURER’S INSTRUCTIONS TELL YOU DIFFERENTLY, DO THE PROCEDURE THAT FOLLOWS." |
| station (v) | NOT APPROVED | use: PUT (v) — "Station a person near the fuel tank." → "PUT A PERSON NEAR THE FUEL TANK." |
| stationary (adj) | NOT APPROVED | use: STABLE (adj); STOP (v) |
| STAY (v) | To continue to be in a location or condition | forms: STAYS, STAYED No other verb forms. |
| steadily (adv) | NOT APPROVED | use: CONTINUOUSLY (adv) — "If the temperature increases steadily, stop the engine." → "IF THE TEMPERATURE INCREASES CONTINUOUSLY, STOP THE ENGINE." |
| steady (adj) | NOT APPROVED | use: STABLE (adj) — "Make sure that the system pressure is steady." → "MAKE SURE THAT THE SYSTEM PRESSURE IS STABLE." |
| STEP (n) | A specified part of a procedure |  |
| stick (v) | NOT APPROVED | use: ATTACH (v); FREELY (adv); CATCH (v) |
| sticky (adj) | NOT APPROVED | use: TACKY (adj) — "Put the patch on the surface when the cement is sticky." → "WHEN THE CEMENT IS TACKY, PUT THE PATCH ON THE SURFACE." |
| stiff (adj) | NOT APPROVED | use: MOVE (v) — "If the piston is stiff, check the dimensions of the piston and sleeve." → "IF THE PISTON DOES NOT MOVE EASILY IN THE SLEEVE, DO A DIMENSIONAL INSPECTION OF THE PARTS." |
| still (adv) | NOT APPROVED | use: STAY (v); CONTINUE (v) |
| stimulate (v) | NOT APPROVED | use: INCREASE (v) — "Stimulate the airflow." → "INCREASE THE AIRFLOW." |
| stir (v) | NOT APPROVED | use: MIX (v) — "Stir the bonding material with a spatula." → "MIX THE BONDING MATERIAL WITH A SPATULA." |
| STOP (v) | 1. To cause the end of a procedure, movement, or an operation 2. To come to an end | forms: STOPS, STOPPED, STOPPED |
| store (v) | NOT APPROVED | use: KEEP (v); CONTAIN (v); STORAGE (TN) |
| STOW (v) | To move or cause to move into a specified position of storage. | forms: STOWS, STOWED, STOWED |
| STRAIGHT (adj) | Without curves or bends | forms: (STRAIGHTER, STRAIGHTEST) |
| straighten (v) | NOT APPROVED | use: STRAIGHT (adj) — "Do not try to straighten the bends in the cable." → "DO NOT TRY TO MAKE THE BENDS IN THE CABLE STRAIGHT." |
| strain (v) | NOT APPROVED | use: FILTER (TN); STRAIN (TN) |
| strap (v) | NOT APPROVED | use: ATTACH (v) — (WITH STRAPS [TN]) — "Strap the cables to the structure." → "ATTACH THE CABLES TO THE STRUCTURE WITH AN APPLICABLE STRAP." |
| stress (v) | NOT APPROVED | use: FORCE (TN) — "Do not stress the ducting unnecessarily." → "DO NOT PUT TOO MUCH FORCE ON THE DUCTING." |
| strictly (adv) | NOT APPROVED | use: FULLY (adv) — "Strictly obey the safety precautions." → "FULLY OBEY THE SAFETY PRECAUTIONS." |
| strike (v) | NOT APPROVED | use: HIT (v) — "Make certain that the sling does not strike the surface." → "MAKE SURE THAT THE SLING DOES NOT HIT THE SURFACE." |
| STRIP (n) | A piece of material that is long and thin, but not wide |  |
| strip (v) | NOT APPROVED | use: REMOVE (v) — "Strip the insulation from the wire." → "REMOVE THE INSULATION FROM THE WIRE." |
| STRIPE (n) | A line on a surface which is a different color |  |
| striped (adj) | NOT APPROVED | use: STRIPE (n) — "The flag is striped red and white." → "THE FLAG HAS RED AND WHITE STRIPES." |
| stroke (n) | NOT APPROVED | use: TRAVEL (n) — "Bleed the braking system by applying full strokes to the hand pump handle." → "TO BLEED THE BRAKING SYSTEM, OPERATE THE HAND PUMP HANDLE THROUGH ITS FULL TRAVEL." |
| STRONG (adj) | With much strength, power, or concentration | forms: (STRONGER, STRONGEST) |
| STRUCTURAL (adj) | Related to the structure |  |
| STRUCTURALLY (adv) | Related to the structure |  |
| STRUCTURE (n) | 1. A construction 2. The arrangement of something |  |
| SUBASSEMBLY (n) | An assembly that is a part of a larger assembly |  |
| submerge (v) | NOT APPROVED | use: PUT (v) — "Submerge the filter element in the fluid." → "PUT THE FILTER ELEMENT FULLY INTO THE FLUID." |
| submit (v) | NOT APPROVED | use: SEND (v) — "Submit the metal particles to a laboratory for analysis." → "SEND THE METAL PARTICLES TO A LABORATORY FOR ANALYSIS." |
| SUBSEQUENT (adj) | Following in an unspecified time or sequence Use NEXT (adj) for the first occurrence that follows immediately in time or sequence. |  |
| SUBSEQUENTLY (adv) | After an unspecified time Use THEN (adv) for an occurrence that follows immediately in time or sequence. |  |
| subsequent to (prep) | NOT APPROVED | use: AFTER (conj) — "Remove the handling tool subsequent to the installation of the component." → "AFTER YOU INSTALL THE COMPONENT, REMOVE THE HANDLING TOOL." |
| substance (n) | NOT APPROVED | use: MATERIAL (n) — "The primer contains a substance that prevents corrosion." → "THE PRIMER CONTAINS A MATERIAL THAT PREVENTS CORROSION." |
| substitute (adj) | NOT APPROVED | use: EQUIVALENT (adj); ALTERNATIVE (adj) |
| substitute (n) | NOT APPROVED | use: ALTERNATIVE (n) — "Equivalent substitutes may be used for these items." → "YOU CAN USE ALTERNATIVES FOR THESE ITEMS." |
| substitute (v) | NOT APPROVED | use: REPLACE (v) — "Do not substitute the self-locking nuts with plain nuts." → "DO NOT REPLACE THE SELF-LOCKING NUTS WITH PLAIN NUTS." |
| SUBTRACT (v) | To take from a number or quantity | forms: SUBTRACTS, SUBTRACTED, SUBTRACTED |
| successful (adj) | NOT APPROVED | use: CORRECT (adj); SATISFACTORY (adj) |
| SUCH (adj) | Of the same group |  |
| suck (v) | NOT APPROVED | use: REMOVE (v) — (WITH SUCTION [TN]) — "Suck out the unwanted material." → "REMOVE THE UNWANTED MATERIAL WITH SUCTION." |
| SUDDEN (adj) | That occurs in a short time |  |
| SUDDENLY (adv) | In a sudden manner |  |
| SUFFICIENT (adj) | Not less (or more) than necessary |  |
| SUFFICIENTLY (adv) | Not less (or more) than necessary |  |
| suitable (adj) | NOT APPROVED | use: APPLICABLE (adj); CORRECT (adj) |
| suitably (adv) | NOT APPROVED | use: SUFFICIENTLY (adv) — "When the paint is suitably soft, remove it with a plastic spatula." → "WHEN THE PAINT IS SUFFICIENTLY SOFT, REMOVE IT WITH A PLASTIC SPATULA." |
| SUM (n) | The result when you add |  |
| SUPPLY (n) | Something that is supplied |  |
| SUPPLY (v) | 1. To give something that is necessary 2. To make something available for use | forms: SUPPLIES, SUPPLIED, SUPPLIED |
| support (n) | NOT APPROVED | use: SUPPORT (TN); HOLD (v) |
| support (v) | NOT APPROVED | use: HOLD (v); SUPPORT (TN) |
| SURE (adj) | Certain |  |
| SURFACE (n) | One or more of the faces of something |  |
| surplus (adj) | NOT APPROVED | use: UNWANTED (adj) — "Wipe off surplus grease." → "REMOVE THE UNWANTED GREASE." |
| surrounding (adj) | NOT APPROVED | use: ADJACENT (adj); AROUND (prep) |
| survey (v) | NOT APPROVED | use: EXAMINE (v); INSPECTION (n) |
| suspect (adj) | NOT APPROVED | use: THINK (v) — "Remove the suspect valve." → "IF YOU THINK THAT THE VALVE IS UNSERVICEABLE, REMOVE IT." |
| suspect (v) | NOT APPROVED | use: THINK (v) — "If you suspect that the power unit does not operate correctly, do a system check." → "IF YOU THINK THAT THE POWER UNIT DOES NOT OPERATE CORRECTLY, DO A SYSTEM CHECK." |
| suspend (v) | NOT APPROVED | use: HANG (v); STOP (v) |
| SWALLOW (v) | To take through the mouth and esophagus into the stomach Use this word for safety instructions only. | forms: SWALLOWS, SWALLOWED, SWALLOWED |
| swap (v) | NOT APPROVED | use: INTERCHANGE (v) — "Swap computers 1 and 2. Then do the test again." → "INTERCHANGE THE COMPUTERS 1 AND 2. THEN DO THE TEST AGAIN." |
| sweep (v) | NOT APPROVED | use: SCAN (TN) — "Sweep the frequency band." → "MAKE A SCAN OF THE FREQUENCY BAND." |
| swing (v) | NOT APPROVED | use: MOVE (v); CALIBRATE (v) |
| switch (v) | NOT APPROVED | use: SET (v) — "Switch the selector to “SYSTEM DISPLAY.”" → "SET THE SELECTOR TO “SYSTEM DISPLAY.”" |
| switch off (v) | NOT APPROVED | use: SET (v); STOP (v); DE-ENERGIZE (v) |
| switch on (v) | NOT APPROVED | use: SET (v); START (v); ENERGIZE (v) |
| SYMBOL (n) | A written sign that identifies a quantity, operation, item, or condition |  |
| SYMMETRICAL (adj) | That has or is with symmetry |  |
| SYMMETRICALLY (adv) | In a symmetrical manner |  |
| SYMPTOM (n) | A sign of a condition |  |
| synchronize (v) | NOT APPROVED | use: ADJUST (v) — "Synchronize compass system 1 with compass system 2." → "ADJUST COMPASS SYSTEM 1 UNTIL IT AGREES WITH COMPASS SYSTEM 2." |
| SYNCHRONIZED (adj) | 1. That operates at the same time 2. That agrees with |  |
| SYSTEM (n) | An assembly of related parts to do a specified operation |  |
| TACKY (adj) | Sticky when you touch it | forms: No other forms of this adjective |
| TAG (v) | To put a tag on | forms: TAGS, TAGGED, TAGGED |
| take (v) | NOT APPROVED | use: REMOVE (v); READ (v); GET (v); NECESSARY (adj) |
| take care (v) | NOT APPROVED | use: MAKE SURE (v); OBEY (v); DO NOT (v); CAREFUL (adj) |
| talk (v) | NOT APPROVED | use: SPEAK (v) — "Talk into the microphone." → "SPEAK INTO THE MICROPHONE." |
| TAP (v) | To hit lightly and quickly | forms: TAPS, TAPPED, TAPPED |
| tape (v) | NOT APPROVED | use: TAPE (TN) — "Tape the foil in position." → "ATTACH THE FOIL WITH TAPE TO KEEP IT IN POSITION." |
| TASK (n) | Assigned work or procedure |  |
| taut (adj) | NOT APPROVED | use: TENSION (TN) — "Make sure the cables are taut." → "MAKE SURE THAT THE TENSION IN THE CABLES IS CORRECT." |
| tear (v) | NOT APPROVED | use: DAMAGE (n) — "Take care you do not tear the bellows." → "BE CAREFUL THAT YOU DO NOT CAUSE DAMAGE TO THE BELLOWS." |
| technique (n) | NOT APPROVED | use: METHOD (n) — "This technique gives the best results." → "THIS METHOD GIVES THE BEST RESULTS." |
| TELESCOPIC (adj) | Related to items that retract into each other |  |
| TELL (v) | To give an order or supply information | forms: TELLS, TOLD, TOLD |
| TEMPORARILY (adv) | In a temporary manner |  |
| TEMPORARY (adj) | For a short time only, not permanent |  |
| tension (v) | NOT APPROVED | use: TENSION (TN) — "Tension cables to the correct value." → "ADJUST THE TENSION IN THE CABLES TO THE CORRECT VALUE." |
| terminate (v) | NOT APPROVED | use: STOP (v) — "Terminate the test after 2 seconds." → "STOP THE TEST AFTER 2 SECONDS." |
| TERTIARY (adj) | Third in importance |  |
| TEST (n) | The procedure where an object or system is operated to make sure that its performance and/or function is correct |  |
| test (v) | NOT APPROVED | use: TEST (n) — "Functionally test the software." → "DO A FUNCTIONAL TEST OF THE SOFTWARE." |
| THAN (conj) | Function word that you use with comparative adjectives or adverbs |  |
| THAT (conj) | Function word that starts a subordinate clause | Refer to section 9, GR-1. |
| THAT (pron) | Function word that shows the person or thing referred to |  |
| THE (art) | Function word: definite article |  |
| THEIR (adj) | Belonging to persons or things |  |
| THEM (pron) | Function word that shows the persons or things referred to |  |
| THEN (adv) | Immediately after in time or sequence |  |
| THERE (adv) | In that position |  |
| THERE (pron) | Function word that starts a sentence or a subordinate clause |  |
| therefore (adv) | NOT APPROVED | use: THUS (adv); AS A RESULT |
| THESE (adj) | Refers to specified persons or things |  |
| THESE (pron) | Function word that shows the persons or things referred to |  |
| THEY (pron) | Function word that shows the persons or things referred to |  |
| THICK (adj) | That has a specified or large thickness | forms: (THICKER, THICKEST) |
| THICKNESS (n) | The smallest of the three dimensions |  |
| THIN (adj) | That has a small thickness | forms: (THINNER, THINNEST) |
| thin (v) | NOT APPROVED | use: LIQUID (adj) — "Add solvent to thin the paint." → "ADD SOLVENT TO MAKE THE PAINT MORE LIQUID." |
| THINK (v) | To have an opinion | forms: THINKS, THOUGHT, THOUGHT |
| THIS (adj) | Refers to a specified person or thing |  |
| THIS (pron) | Function word that shows the person or thing referred to | Refer to section 9, GR-4. |
| thorough (adj) | NOT APPROVED | use: FULL (adj) — "Do a thorough check of the control system." → "DO A FULL CHECK OF THE CONTROL SYSTEM." |
| thoroughly (adv) | NOT APPROVED | use: FULLY (adv) — "Dry the surface thoroughly." → "DRY THE SURFACE FULLY." |
| THOSE (pron) | Function word that shows the persons or things referred to |  |
| thread (v) | NOT APPROVED | use: PUT (v); TURN (v) |
| threaded (adj) | NOT APPROVED | use: THREAD (TN) — "Put the threaded end of the rod in the fitting." → "PUT THE END OF THE ROD THAT HAS A THREAD IN THE FITTING." |
| THROUGH (adv) | Function word that shows movement into one end or side and out of the other |  |
| THROUGH (prep) | Function word that shows movement into one end or side and out of the other |  |
| throughout (prep) | NOT APPROVED | use: DURING (prep) — "Make sure that the doors are closed throughout the test." → "MAKE SURE THAT THE DOORS ARE CLOSED DURING THE TEST." |
| THRU (prep) | From a point in a sequence to another |  |
| THUS (adv) | For that reason | For other meanings, use: FOLLOW (v) |
| tie (v) | NOT APPROVED | use: ATTACH (v) — "Tie the threading cord to the new cable." → "ATTACH THE THREADING CORD TO THE NEW CABLE." |
| TIGHT (adj) | Not free | For other meanings, use: SEAL (v); TENSION (TN); forms: (TIGHTER, TIGHTEST) |
| TIGHTEN (v) | To cause to be tight | forms: TIGHTENS, TIGHTENED, TIGHTENED |
| TIGHTLY (adv) | In a tight manner |  |
| till (conj) | NOT APPROVED | use: UNTIL (conj) — "Move the lever till it hits the stop." → "MOVE THE LEVER UNTIL IT TOUCHES THE STOP." |
| TILT (v) | To move at an angle or to put something at an angle between the vertical and the horizontal | forms: TILTS, TILTED, TILTED |
| TIME (n) | 1. A duration that you can measure 2. An occurrence |  |
| time (v) | NOT APPROVED | use: TIME (n) — "Time the pressure decay." → "MEASURE THE TIME THAT IS NECESSARY FOR THE PRESSURE TO DECREASE." |
| tip (n) | NOT APPROVED | use: POINT (n) — "Before you make the hole, make sure the tip of the drill bit is sharp." → "BEFORE YOU MAKE THE HOLE, MAKE SURE THAT THE POINT OF THE DRILL BIT IS SHARP." |
| tip (v) | NOT APPROVED | use: TILT (v) — "To install the indicator, tip it rearward." → "TO INSTALL THE INDICATOR, TILT IT REARWARD." |
| TO (prep) | Function word that shows: - The direction of, point of arrival or time, connection, result, cause - That the word that follows is an infinitive |  |
| TOGETHER (adv) | In one group or position | For other meanings, use: AT THE SAME TIME |
| TOLERANCE (n) | A permitted difference from a standard |  |
| TOO (adv) | More than is necessary or correct |  |
| TOOL (n) | An object used to make or do something |  |
| TOP (adj) | That is uppermost |  |
| TOP (n) | The uppermost position |  |
| top off (v) | NOT APPROVED | use: FILL (v); ADD (v) |
| TORQUE (v) | To tighten to a specified torque | forms: TORQUES, TORQUED, TORQUED |
| TOTAL (adj) | All of |  |
| TOTAL (n) | The full quantity |  |
| TOUCH (v) | To be in contact | forms: TOUCHES, TOUCHED, TOUCHED |
| TOW (v) | To pull something along | forms: TOWS, TOWED, TOWED |
| toward (prep) | NOT APPROVED | use: TO (prep); DIRECTION (n) |
| toxic (adj) | NOT APPROVED | use: POISONOUS (adj) — "This compound is toxic." → "THIS COMPOUND IS POISONOUS." |
| trace (n) | NOT APPROVED | use: SIGN (n) — "Check the area surrounding the drain holes for traces of corrosion." → "EXAMINE THE AREA AROUND THE DRAIN HOLES FOR SIGNS OF CORROSION." |
| trace (v) | NOT APPROVED | use: FIND (v) — "Trace the broken wire." → "FIND THE BROKEN WIRE." |
| track (v) | NOT APPROVED | use: MONITOR (v) — "Track the temperature." → "MONITOR THE TEMPERATURE." |
| trained (adj) | NOT APPROVED | use: APPROVED (adj) — "Only trained personnel can operate the brakes." → "ONLY APPROVED PERSONNEL CAN OPERATE THE BRAKES." |
| transfer (n) | NOT APPROVED | use: MOVEMENT (n); SUPPLY (n) |
| transfer (v) | NOT APPROVED | use: MOVE (v); INSTALL (v) |
| transition (n) | NOT APPROVED | use: CHANGE (n) — "The transition from full-rate operation to half-rate operation must occur immediately." → "THE CHANGE FROM FULL-RATE OPERATION TO HALF-RATE OPERATION MUST OCCUR IMMEDIATELY." |
| TRANSMIT (v) | To send energy or a signal | forms: TRANSMITS, TRANSMITTED, TRANSMITTED |
| TRANSPARENT (adj) | Easy to see through |  |
| transport (v) | NOT APPROVED | use: SEND (v) — "Transport the part to the overhaul shop." → "SEND THE PART TO THE OVERHAUL SHOP." |
| trapped (adj) | NOT APPROVED | use: CAUGHT (adj) — "Make sure that the cable is not trapped." → "MAKE SURE THAT THE CABLE IS NOT CAUGHT." |
| TRAVEL (n) | The movement of an item |  |
| travel (v) | NOT APPROVED | use: GO (v); MOVE (v) |
| treat (v) | NOT APPROVED | use: APPLY (v); TOUCH (v) |
| trigger (v) | NOT APPROVED | use: CAUSE (v); START (v) |
| trim (v) | NOT APPROVED | use: CUT (v) — "Trim the patch to fit." → "CUT THE PATCH TO THE CORRECT DIMENSION." |
| trip (v) | NOT APPROVED | use: OPEN (v); RELEASE (v); CAUSE TO FALL |
| troubleshoot (v) | NOT APPROVED | use: TROUBLESHOOTING (TN) — "Troubleshoot the VHF navigation system." → "DO THE TROUBLESHOOTING PROCEDURE ON THE VHF NAVIGATION SYSTEM." |
| true (adj) | NOT APPROVED | use: CORRECT (adj); AGREE (v) |
| TRY (v) | To make an effort to do something | forms: TRIES, TRIED, TRIED |
| tuck (v) | NOT APPROVED | use: PUT (v) — "Tuck the headstrap into the face piece." → "PUT THE HEADSTRAP INTO THE FACE PIECE." |
| TUNE (v) | To adjust equipment to the best performance | forms: TUNES, TUNED, TUNED |
| TURN (n) | One full cycle of movement around an axis |  |
| TURN (v) | To move or cause to move around an axis or a point | forms: TURNS, TURNED, TURNED |
| turn off (v) | NOT APPROVED | use: SET (v); STOP (v); DE-ENERGIZE (v) |
| turn on (v) | NOT APPROVED | use: SET (v); START (v); ENERGIZE (v) |
| turn over (v) | NOT APPROVED | use: TURN (v) — "Turn the display panel over to access the cable." → "TURN THE DISPLAY PANEL UNTIL YOU HAVE ACCESS TO THE CABLE." |
| twice (adv) | NOT APPROVED | use: TWO (TN) — "Do this procedure twice." → "DO THIS PROCEDURE TWO TIMES." |
| TWIST (v) | 1. To use a force that turns something and causes a distortion 2. To turn or change shape as a result of torsion | forms: TWISTS, TWISTED, TWISTED |
| TYPE (n) | A specified group |  |
| TYPICAL (adj) | That has the important qualities of a group |  |
| unable (adj) | NOT APPROVED | use: CANNOT (v) — "If you are unable to turn the pulley, make sure that the pin is removed." → "IF YOU CANNOT TURN THE PULLEY, MAKE SURE THAT THE PIN IS REMOVED." |
| unauthorized (adj) | NOT APPROVED | use: NOT APPROVED — "If you are unauthorized, do not do this engine test." → "IF YOU ARE NOT APPROVED TO DO THIS WORK, DO NOT DO THIS ENGINE TEST." |
| uncap (v) | NOT APPROVED | use: REMOVE (v) — (A CAP [TN] OR CAPS [TN]) — "Uncap the hoses." → "REMOVE THE CAPS FROM THE HOSES." |
| unclip (v) | NOT APPROVED | use: REMOVE (v) — (FROM A CLIP [TN] OR CLIPS [TN]) — "Unclip the visor." → "REMOVE THE VISOR FROM THE CLIP." |
| uncoil (v) | NOT APPROVED | use: UNWIND (v) — "Uncoil the cables carefully." → "UNWIND THE CABLES CAREFULLY." |
| uncontaminated (adj) | NOT APPROVED | use: CLEAN (adj); CONTAMINATION (n) |
| uncouple (v) | NOT APPROVED | use: DISCONNECT (v) — "Uncouple the tow bar from the vehicle." → "DISCONNECT THE TOW BAR FROM THE VEHICLE." |
| uncovered (adj) | NOT APPROVED | use: COVER (TN) — "Leave the container uncovered." → "DO NOT PUT A COVER ON THE CONTAINER." |
| undamaged (adj) | NOT APPROVED | use: NOT DAMAGED — "Make sure that the skin is undamaged." → "MAKE SURE THAT THE SKIN IS NOT DAMAGED." |
| UNDEMANDED (adj) | That occurs without an apparent cause |  |
| under (prep) | NOT APPROVED | use: BELOW (prep); IN (prep); LESS THAN |
| underneath (prep) | NOT APPROVED | use: BELOW (prep) — "Place the container underneath the drain valve." → "PUT THE CONTAINER BELOW THE DRAIN VALVE." |
| underside (n) | NOT APPROVED | use: BOTTOM (n) — "Examine the four attaching holes on the underside." → "EXAMINE THE FOUR ATTACHING HOLES ON THE BOTTOM." |
| undertake (v) | NOT APPROVED | use: DO (v); START (v) — You can use a more accurate verb. |
| undo (v) | NOT APPROVED | use: LOOSEN (v) — "Undo the bolts that attach the unit." → "LOOSEN THE BOLTS THAT ATTACH THE UNIT." |
| undue (adj) | NOT APPROVED | use: UNWANTED (adj) — "To prevent undue friction, polish the surface." → "TO PREVENT UNWANTED FRICTION, POLISH THE SURFACE." |
| uneven (adj) | NOT APPROVED | use: EQUAL (adj); ROUGH (adj) |
| UNFOLD (v) | To open or to straighten or to cause to open or to straighten from a folded position or condition | forms: UNFOLDS, UNFOLDED, UNFOLDED |
| uniform (adj) | NOT APPROVED | use: CONSTANT (adj); EQUAL (adj) |
| uniformly (adv) | NOT APPROVED | use: EQUALLY (adv) — "Make sure that the two pistons extend uniformly." → "MAKE SURE THAT THE TWO PISTONS EXTEND EQUALLY." |
| unintentional (adj) | NOT APPROVED | use: ACCIDENTAL (adj) — "A guard on the control switch of the pump prevents unintentional operation." → "A GUARD ON THE CONTROL SWITCH OF THE PUMP PREVENTS ACCIDENTAL OPERATION." |
| unintentionally (adv) | NOT APPROVED | use: ACCIDENTALLY (adv) — "If rain repellent fluid is unintentionally sprayed onto a dry windshield, remove the fluid with solvent." → "IF YOU ACCIDENTALLY SPRAY RAIN REPELLENT FLUID ONTO A DRY WINDSHIELD, REMOVE THE FLUID WITH SOLVENT." |
| UNIT (n) | 1. Equipment that does a function 2. A quantity that is a standard of measurement |  |
| UNKNOWN (adj) | Not known |  |
| unlatch (v) | NOT APPROVED | use: RELEASE (v); OPEN (v) |
| UNLESS (conj) | Except if |  |
| unload (v) | NOT APPROVED | use: RELEASE (v); LOAD (TN) |
| UNLOCK (v) | To release or become released from a locked condition | forms: UNLOCKS, UNLOCKED, UNLOCKED |
| unnecessary (adj) | NOT APPROVED | use: NOT NECESSARY — "Remove the unnecessary ground equipment." → "REMOVE THE GROUND EQUIPMENT THAT IS NOT NECESSARY." |
| unobstructed (adj) | NOT APPROVED | use: CLOGGED (adj); CLEAR (adj) |
| unpack (v) | NOT APPROVED | use: REMOVE (v) — "Unpack the shipping container." → "REMOVE THE PARTS FROM THE SHIPPING CONTAINER." |
| unpainted (adj) | NOT APPROVED | use: BARE (adj) — "Protect the unpainted surfaces." → "APPLY PROTECTIVE TREATMENT ON THE BARE SURFACES." |
| unplug (v) | NOT APPROVED | use: DISCONNECT (v); PLUG (TN) |
| unprotected (adj) | NOT APPROVED | use: PROTECTION (n) — "When you remove the cover, the contacts are unprotected." → "WHEN YOU REMOVE THE COVER, THE CONTACTS HAVE NO PROTECTION." |
| unreel (v) | NOT APPROVED | use: UNWIND (v) — "Unreel the hose." → "UNWIND THE HOSE." |
| unrestricted (adj) | NOT APPROVED | use: FREE (adj) — "Ball bearing rotation must be unrestricted." → "THE BALL BEARING MUST BE FREE TO TURN." |
| unsafe (adj) | NOT APPROVED | use: DANGEROUS (adj) — "In these conditions, it is unsafe to remove the cartridges from the fire extinguisher bottle." → "IN THESE CONDITIONS, IT IS DANGEROUS TO REMOVE THE CARTRIDGES FROM THE FIRE EXTINGUISHER BOTTLE." |
| UNSATISFACTORILY (adv) | In an unsatisfactory manner |  |
| UNSATISFACTORY (adj) | Not satisfactory |  |
| unscrew (v) | NOT APPROVED | use: LOOSEN (v); TURN (v); REMOVE (v) |
| UNSERVICEABLE (adj) | Not fit for its purpose |  |
| unstable (adj) | NOT APPROVED | use: NOT STABLE — "If the surface is unstable, an accident can occur." → "IF THE SURFACE IS NOT STABLE, AN ACCIDENT CAN OCCUR." |
| UNTIL (conj) | Up to the time that |  |
| UNTIL (prep) | Up to the time of |  |
| unused (adj) | NOT APPROVED | use: NEW (adj) — "Fill the tank with unused oil." → "FILL THE TANK WITH NEW OIL." |
| UNUSUAL (adj) | Not usual |  |
| UNUSUALLY (adv) | In an unusual manner |  |
| UNWANTED (adj) | That must not be there |  |
| UNWIND (v) | To remove or become removed from around an object | forms: UNWINDS, UNWOUND, UNWOUND |
| UP (adj) | In a position above |  |
| UP (adv) | To a position above |  |
| UP (prep) | To a position above |  |
| upon (prep) | NOT APPROVED | use: ON (prep); WHEN (conj) |
| upper (adj) | NOT APPROVED | use: MAXIMUM (adj); TOP (adj) |
| uppermost (adj) | NOT APPROVED | use: UP (adv) — "Install the bolts with their heads in uppermost position." → "INSTALL THE BOLTS WITH THEIR HEADS UP." |
| uppermost (adv) | NOT APPROVED | use: UP (adv) — "Install the bolts with their heads uppermost." → "INSTALL THE BOLTS WITH THEIR HEADS UP." |
| UPSTREAM (adj) | In a direction opposite to the flow |  |
| UPSTREAM (adv) | In a direction opposite to the flow |  |
| UPSTREAM OF (prep) | In a direction opposite to the flow |  |
| up to (prep) | NOT APPROVED | use: UNTIL (prep); THRU (prep); MAXIMUM (n) |
| upward (adv) | NOT APPROVED | use: UP (adv) — "Move the lever upward." → "MOVE THE LEVER UP." |
| urgently (adv) | NOT APPROVED | use: IMMEDIATELY (adv) — "Seek medical aid urgently." → "GET MEDICAL AID IMMEDIATELY." |
| usage (n) | NOT APPROVED | use: USE (v) — "The usage of incorrect thinners can cause problems during operation." → "IF YOU USE INCORRECT THINNERS. PROBLEMS CAN OCCUR DURING OPERATION." |
| use (n) | NOT APPROVED | use: OPERATION (n); USE (v) |
| USE (v) | To make something do its specified function | forms: USES, USED, USED |
| USUAL (adj) | That you use or that occurs most frequently |  |
| USUALLY (adv) | In a usual manner |  |
| utilization (n) | NOT APPROVED | use: USE (v) — "Read the oxygen mask instructions for its utilization." → "READ THE INSTRUCTIONS THAT TELL YOU HOW TO USE THE OXYGEN MASK." |
| utilize (v) | NOT APPROVED | use: USE (v) — "The software utilizes caching techniques to decrease data retrieval times." → "THE SOFTWARE USES CACHING TECHNIQUES TO DECREASE DATA RETRIEVAL TIMES." |
| valid (adj) | NOT APPROVED | use: CORRECT (adj); APPLICABLE (adj) — This word becomes part of a technical noun when it refers to an official document. |
| validity (n) | NOT APPROVED | use: CORRECT (adj); APPLICABLE (adj) |
| VALUE (n) | A quantity that is calculated or given |  |
| variable (adj) | NOT APPROVED | use: CHANGE (v) — "If the humidity is variable, put a cover on the unit." → "IF THE HUMIDITY CHANGES FREQUENTLY, PUT A COVER ON THE UNIT." |
| various (adj) | NOT APPROVED | use: DIFFERENT (adj) — "Refer to Table 5 for the various torque values that are applicable to the unit." → "REFER TO TABLE 5 FOR THE DIFFERENT TORQUE VALUES THAT ARE APPLICABLE TO THE UNIT." |
| vary (v) | NOT APPROVED | use: CHANGE (v) — "Vary the frequency and record the results." → "CHANGE THE FREQUENCY AND RECORD THE RESULTS." |
| vent (v) | NOT APPROVED | use: RELEASE (v); FLOW (v); OPEN (adj) |
| ventilate (v) | NOT APPROVED | use: AIRFLOW (n) — "Ventilate the area where this solvent is used." → "MAKE SURE THAT THE AREA WHERE YOU WILL USE THIS SOLVENT HAS GOOD AIRFLOW." |
| ventilation (n) | NOT APPROVED | use: AIRFLOW (n) — "Make sure that the ventilation is sufficient." → "MAKE SURE THAT THE AIRFLOW IS SUFFICIENT." |
| verify (v) | NOT APPROVED | use: MAKE SURE (v) — "Verify the tightness of the fittings." → "MAKE SURE THAT THE FITTINGS ARE TIGHT." |
| VERTICAL (adj) | At 90 degrees to the horizon |  |
| VERTICALLY (adv) | At 90 degrees to the horizon |  |
| VERY (adv) | To a high degree |  |
| via (prep) | NOT APPROVED | use: THROUGH (prep) — "Get access via No. 6 break-in panel." → "GET ACCESS THROUGH THE No. 6 BREAK-IN PANEL." |
| vibrate (v) | NOT APPROVED | use: VIBRATION (n) — "If the unit vibrates, cut the power." → "IF THERE IS VIBRATION IN THE UNIT, DISCONNECT THE POWER SUPPLY." |
| VIBRATION (n) | Regular movement from a center position |  |
| vicinity (n) | NOT APPROVED | use: NEAR (prep); ADJACENT (adj) |
| VIEW (n) | The ability to see something |  |
| view (v) | NOT APPROVED | use: SEE (v); LOOK (v) |
| vigorous (adj) | NOT APPROVED | use: FORCE (TN) — "Vigorous cleaning with a brush can cause damage to the carpet." → "WHEN YOU CLEAN THE CARPET, DO NOT USE TOO MUCH FORCE ON THE BRUSH. TOO MUCH FORCE CAN CAUSE DAMAGE TO THE CARPET." |
| vigorously (adv) | NOT APPROVED | use: FORCE (TN) — "Do not move the control wheel too vigorously." → "WHEN YOU MOVE THE CONTROL WHEEL, DO NOT APPLY TOO MUCH FORCE." |
| visible (adj) | NOT APPROVED | use: SEE (v); VIEW (n) |
| VISUAL (adj) | That you can see |  |
| VISUALLY (adv) | With the eyes |  |
| vital (adj) | NOT APPROVED | use: MANDATORY (adj) — "It is vital to obey the supplier’s maintenance intervals." → "IT IS MANDATORY TO OBEY THE SUPPLIER’S MAINTENANCE INTERVALS." |
| VOICE (n) | The sound you make when you speak |  |
| volatile (adj) | NOT APPROVED | Use a different construction. Tell the reader what the risk or effect is. — "Be careful with the solvent (this solvent is volatile and can be dangerous)." → "BE CAREFUL WITH THE SOLVENT NEAR FLAMES OR SPARKS. THIS SOLVENT CAN RELEASE FLAMMABLE FUMES." |
| VOLUME (n) | 1. The space that an object fills 2. How loud a sound is |  |
| WAIT (v) | To stop doing something while another thing occurs. | forms: WAITS, WAITED, WAITED |
| WALK (v) | To move on foot from one location to a different location | forms: WALKS, WALKED, WALKED |
| WANT (v) | To intend, to desire | forms: WANTS, WANTED, WANTED |
| WARM (adj) | Moderately hot |  |
| warm (v) | NOT APPROVED | use: WARM (adj) — "Warm the mixture before use." → "MAKE THE MIXTURE WARM BEFORE YOU USE IT." |
| warn (v) | NOT APPROVED | use: TELL (v); WARNING (TN) |
| wash (v) | NOT APPROVED | use: CLEAN (v) — "Wash your hands using soap." → "CLEAN YOUR HANDS WITH SOAP." |
| watch (v) | NOT APPROVED | use: MONITOR (v); LOOK (v) |
| watertight (adj) | NOT APPROVED | use: SEAL (v) — "Check that the tank is watertight." → "MAKE SURE THAT THE TANK IS SEALED." |
| way (n) | NOT APPROVED | use: PROCEDURE (n) — "Do not use other ways to replace the unit." → "DO NOT USE OTHER PROCEDURES TO REPLACE THE UNIT." |
| WE (pron) | The manufacturer, company, or organization that releases the documentation | Do not use this pronoun for other meanings. |
| WEAK (adj) | With small strength, power, or concentration | forms: (WEAKER, WEAKEST) |
| weakness (n) | NOT APPROVED | use: WEAK (adj) — "There is a point of weakness in the strut." → "THERE IS A WEAK POINT IN THE STRUT." |
| WEAR (v) | To become damaged by friction | For other meanings, use: USE (v); PUT ON (v); forms: WEARS, WORE, WORN |
| WEATHER (n) | Conditions of the atmosphere: temperature, moisture, winds, and clouds |  |
| weep (n) | NOT APPROVED | use: LEAKAGE (n) — "If there are fuel weeps from the couplings, reject the unit." → "IF THERE IS FUEL LEAKAGE FROM THE COUPLINGS, REJECT THE UNIT." |
| WEIGH (v) | 1. To measure the weight of something 2. To have a specified weight | forms: WEIGHS, WEIGHED, WEIGHED |
| WEIGHT (n) | The force caused when gravity acts on the mass of an object |  |
| well (adv) | NOT APPROVED | use: CORRECTLY (adv); GOOD (adj); FULLY (adv) |
| WET (adj) | That has liquid on it, in it, or absorbed into it | forms: (WETTER, WETTEST) |
| WHEN (conj) | At the time that or during |  |
| whenever (conj) | NOT APPROVED | use: WHEN (conj) — "Stop the test whenever the pressure is more than 7000 kPa." → "WHEN THE PRESSURE IS MORE THAN 7000 kPa, STOP THE TEST." |
| WHERE (conj) | At, to, or in which location |  |
| whether (conj) | NOT APPROVED | use: IF (conj) — "This limit applies whether the aircraft is on the landing gear or on jacks." → "THIS LIMIT IS APPLICABLE IF THE AIRCRAFT IS ON THE LANDING GEAR OR ON JACKS." |
| WHICH (pron) | The thing or things that |  |
| whichever (adj) | NOT APPROVED | use: THAT (pron) — "Use whichever adhesive is available." → "USE THE ADHESIVE THAT IS AVAILABLE." |
| whichever (pron) | NOT APPROVED | use: THAT (pron) — "Different adhesives are permitted. Use whichever is available." → "DIFFERENT ADHESIVES ARE PERMITTED. USE THE ONE THAT IS AVAILABLE." |
| WHILE (conj) | At the same time |  |
| whilst (conj) | NOT APPROVED | use: WHILE (conj) — "Do not open the housing whilst the electrical power is connected." → "DO NOT OPEN THE HOUSING WHILE THE ELECTRICAL POWER IS CONNECTED." |
| WHO (pron) | The person or personnel that |  |
| whoever (pron) | NOT APPROVED | use: WHO (pron) — "Whoever is in this area must use a respirator." → "ALL PERSONS WHO ARE IN THIS AREA MUST USE A RESPIRATOR." |
| whole (adj) | NOT APPROVED | use: FULL (adj); ALL (adj) |
| wholly (adv) | NOT APPROVED | use: FULLY (adv) — "The system is wholly automatic." → "THE SYSTEM IS FULLY AUTOMATIC." |
| whose (pron) | NOT APPROVED | Use a different construction. — "The generators produce a three-phase voltage whose frequency is proportional to the generator rotor speed." → "THE GENERATORS SUPPLY A THREE-PHASE VOLTAGE. THE FREQUENCY OF THIS VOLTAGE INCREASES WHEN THE GENERATOR ROTOR SPEED INCREASES." |
| WIDE (adj) | That has a specified or large width | forms: (WIDER, WIDEST) |
| WIDTH (n) | The smaller of two dimensions, the second- largest of three dimensions |  |
| WILL (v) | Auxiliary modal verb that shows simple future tense | forms: No other verb forms. |
| WIND (v) | To move around and around an object | forms: WINDS, WOUND, WOUND |
| windy (adj) | NOT APPROVED | use: WIND (TN) — "Take special precautions in very windy conditions." → "WHEN THERE ARE STRONG WINDS, OBEY THESE SPECIAL PRECAUTIONS." |
| wipe (v) | NOT APPROVED | use: CLEAN (v) — "Wipe the indicator surfaces before each cycle." → "BEFORE EACH CYCLE, CLEAN THE INDICATOR." |
| wire (v) | NOT APPROVED | use: ATTACH (v) — (WITH WIRE [TN]) — "Wire the hose to the fixture." → "ATTACH THE HOSE TO THE FIXTURE WITH WIRE." |
| wire-lock (v) | NOT APPROVED | use: LOCK (v); SAFETY (v) — (WITH LOCKWIRE [TN]) (WITH SAFETY WIRE [TN]) |
| WITH (prep) | Function word that shows association or relationship, help or sharing, a means or instrument | Refer to section 9, GR-2. |
| withdraw (v) | NOT APPROVED | use: REMOVE (v) — "Withdraw the indicator from the instrument panel." → "REMOVE THE INDICATOR FROM THE INSTRUMENT PANEL." |
| within (prep) | NOT APPROVED | use: IN (prep); IN LESS THAN — IN ... OR LESS |
| WITHOUT (prep) | Not with |  |
| withstand (v) | NOT APPROVED | use: RESISTANT (adj) — "This material can withstand fire." → "THIS MATERIAL IS RESISTANT TO FIRE." |
| WORK (n) | That which you do when you use physical strength, or mental power |  |
| work (v) | NOT APPROVED | use: WORK (n) — "Be careful when you work near fuel tanks." → "BE CAREFUL WHEN YOU DO WORK NEAR FUEL TANKS." |
| would (v) | NOT APPROVED | use: CAN (v) — "Solvents left on the part would corrode the part." → "SOLVENTS THAT STAY ON THE PART CAN CAUSE CORROSION." |
| wrap (v) | NOT APPROVED | use: PUT (v); WIND (v) |
| WRITE (v) | To record data or information as words, letters, or symbols | forms: WRITES, WROTE, WRITTEN |
| wrong (adj) | NOT APPROVED | use: INCORRECT (adj) — "Mark the bellcrank and shaft to prevent wrong installation." → "IDENTIFY THE BELLCRANK AND SHAFT WITH MARKS. THESE MARKS WILL PREVENT AN INCORRECT INSTALLATION." |
| wrongly (adv) | NOT APPROVED | use: INCORRECTLY (adv) — "Damage can occur if hoses are wrongly installed." → "IF THE HOSES ARE INCORRECTLY INSTALLED, DAMAGE CAN OCCUR." |
| YES (adv) | Function word that shows the positive answer to a question |  |
| yet (conj) | NOT APPROVED | use: BUT (conj) — "The nuts should be tightened, yet loose enough to remove by hand." → "TIGHTEN THE NUTS, BUT KEEP THEM SUFFICIENTLY LOOSE TO REMOVE THEM WITH YOUR HAND." |
| yet (adv) | NOT APPROVED | use: AT THIS TIME — "Do not remove the fixture cover yet." → "DO NOT REMOVE THE FIXTURE COVER AT THIS TIME." |
| YOU (pron) | The reader or the user |  |
| YOUR (adj) | Related to the reader or the user |  |
| yourself (pron) | NOT APPROVED | use: YOU (pron) — "Do not use your hands to prevent movement of the LP compressor. If you do, you can cause injury to yourself and damage to the equipment." → "DO NOT USE YOUR HANDS TO PREVENT MOVEMENT OF THE LP COMPRESSOR. IF YOU DO, THE LP COMPRESSOR CAN CAUSE YOU INJURY AND CAN CAUSE DAMAGE TO THE EQUIPMENT." |
| zero (v) | NOT APPROVED | use: ZERO (TN) — "Zero the meter." → "ADJUST THE METER TO ZERO." |

## Needs manual review

Entries below could not be classified confidently by the parser. Raw cell text is verbatim from the source; check against the PDF (PDF page = 149 + page index).

### decontamination (n) — flags: altnp-run-ambiguous (page index 60)

- col1: decontamination (n)
- col2: REMOVE / CONTAMINATION / CLEAN (v)
- STE ex: REMOVE THE / CONTAMINATION / FROM THE / INSTRUMENTS AND / MEDICAL EQUIPMENT. / CLEAN THE AIRCRAFT / IN AN APPROVED / AREA.
- non-STE ex: Do the decontamination / of the instruments and / medical equipment. / The decontamination of / the aircraft shall be done / in an authorized area.

### FOR EXAMPLE — flags: no-pos (page index 105)

- col1: FOR EXAMPLE
- col2: Used to introduce / something chosen as a / typical case
- STE ex: WHEN YOU REMOVE / THE STUD, USE / APPLICABLE TOOLS. / FOR EXAMPLE, USE A / PLASTIC MALLET AND / A PUNCH.

### slip (v) — flags: altnp-run-ambiguous (page index 231)

- col1: slip (v)
- col2: MOVE (v) / REMOVE (v) / CAUSE TO FALL / MOVE ACCIDENTALLY
- STE ex: MOVE THE CARRIAGE / ALONG THE TRACK. / REMOVE THE CLAMP / FROM THE CABLE. / IF OIL SPILLS, CLEAN / THE AREA / IMMEDIATELY. A WET / SURFACE IS / DANGEROUS AND / CAN CAUSE YOU TO / FALL. / MAKE SURE THAT THE / CLUTCH DOES NOT / MOVE ACCIDENTALLY.
- non-STE ex: Slip the carriage along / the track. / Slip the clamp from the / cable. / If oil spills, clean the / area immediately. You / can slip and fall. / Make sure that the / clutch does not slip.

### such as — flags: no-pos (page index 245)

- col1: such as
- col2: FOR EXAMPLE
- STE ex: WHEN YOU REMOVE / THE STUD, USE / APPLICABLE TOOLS. / FOR EXAMPLE, USE A / PLASTIC MALLET AND / A PUNCH.
- non-STE ex: When you remove the / stud, use applicable / tools such as a plastic / mallet and a punch.

