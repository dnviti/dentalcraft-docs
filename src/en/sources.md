# DentalCraft Sources

*Bibliography of the papers, standards, manuals and specifications behind DentalCraft. Edition of 28 November 2026. The living list is `SOURCES.md` in the `dentalcraft` repository; this document is regenerated from it at every release.*

Every paper, book, manual, dataset, standard, RFC and specification that DentalCraft relies on, grouped by area. For each one: authors, year, title, venue, DOI or URL, and where it is used.

The citations of the *Aligners* evidence base come from `dentalcraft-aligners/crates/dca-algo/src/evidence.rs`. The others come from comments and documents in the repositories of the project, from the notes on the scanner and the printer in this repository (`docs/scanner/`, `docs/plan/`), and from the notes of the Blender add-on `blender-ortho-aligner` that DentalCraft ports. Source code of other projects is not copied: where a protocol or a file format was taken from a community project or a vendor document, only the documented facts were used.

DentalCraft is not a certified medical device. Citing a paper does not mean the software is clinically validated. See [`NOTICE.md`](https://github.com/dnviti/dentalcraft/blob/main/NOTICE.md).

## How the entries were checked

Checked on 2026-11-21.

| Check | Result |
| --- | --- |
| DOIs against Crossref (title compared with the entry) | 107 of 114 matched. The other seven: four old *Angle Orthodontist* DOIs (†), one DataCite DOI (‡), and two whose Crossref title is shorter or longer than the printed one (Artun 1987, Museth 2013); the PMID or the record confirmed each of them. |
| PMIDs against PubMed (title and year compared) | 60 of 60 resolved to the same paper (two titles, Artun 1987 and Poppe 2002, differ only in length). |
| DOIs of the algorithm papers cited only in code comments (section 2.5) | Garland, Hoppe, Zheng, Sun, Pinkall, Umeyama, Gelfand, Taubin, Lorensen, Möller, Newcombe and Whelan matched in Crossref. The audit had written these DOIs from memory. |
| arXiv identifiers | Teeth3DS+ and InfiniTAM v3 matched. |
| Web links | Status of each link listed in section 9. |

Marks used in the tables:

- † The DOI is the one PubMed lists for this *Angle Orthodontist* paper (1996 to 2001), but `doi.org` and Crossref do not resolve it. The PMID matched. Use the PMID link.
- ‡ The DOI is registered with DataCite, not Crossref (Eurographics Digital Library). The title, author and year matched.
- Entries with "no DOI; not checked online" are books, a 1958 paper and vendor manuals. They are given as printed in `evidence.rs` and could not be checked against a registry.
- Where Crossref gives the online date instead of the issue date, the year in the table is the year printed in `evidence.rs`.


## 1. Orthodontic and dental evidence

The *Aligners* module declares every numeric default together with its source in `crates/dca-algo/src/evidence.rs` of `dentalcraft-aligners`. The tables and the report of the application are generated from that file, so a value never appears without its citation. The 111 references below mirror that file entry by entry; the Italian finding texts stay in the code. Parameter names are the keys of `PARAMS` in the same file.

### 1.1 Staging, movement predictability and treatment planning

Default step sizes, intervals and planning limits of the *Aligners* module (`dca-algo` staging, setup and schedule).

| Authors | Year | Title | Venue | DOI / PMID | Used in `evidence.rs` |
| --- | --- | --- | --- | --- | --- |
| Castroflorio T, Sedran A, Parrini S, Garino F, Reverdito M, Capuozzo R, et al. | 2023 | Predictability of orthodontic tooth movement with aligners: effect of treatment design | Prog Orthod 24(1):2 | [`10.1186/s40510-022-00453-0`](https://doi.org/10.1186/s40510-022-00453-0)<br>[PMID 36642743](https://pubmed.ncbi.nlm.nih.gov/36642743/) | Parameters `step_linear`, `step_vertical`, `step_rotation`, `step_rotation_round`, `step_angular`, `interval_days` |
| Martinez-Lozano D, Castellanos-Andres D, Lopez-Jimenez AJ | 2024 | Staging of Orthodontic Tooth Movement in Clear Aligner Treatment: Macro-Staging and Micro-Staging - A Narrative Review | Appl Sci 14(15):6690 | [`10.3390/app14156690`](https://doi.org/10.3390/app14156690) | Parameters `step_linear`, `step_vertical`, `seq_overlap`, `collision_tol`, `vertical_auto_max` |
| Simon M, Keilig L, Schwarze J, Jung BA, Bourauel C | 2014 | Treatment outcome and efficacy of an aligner technique - regarding incisor torque, premolar derotation and molar distalization | BMC Oral Health 14:68 | [`10.1186/1472-6831-14-68`](https://doi.org/10.1186/1472-6831-14-68)<br>[PMID 24923279](https://pubmed.ncbi.nlm.nih.gov/24923279/) | Parameters `step_linear`, `step_rotation`, `step_rotation_round`, `step_angular`, `lag_speed` |
| Wang Y, Chen J, Qin S, Han X, Liao L, Sima X, et al. | 2023 | An in vivo evaluation of clear aligners for optimal orthodontic force and movement to determine high-efficacy and periodontal-friendly aligner staging | Heliyon 9(4):e15317 | [`10.1016/j.heliyon.2023.e15317`](https://doi.org/10.1016/j.heliyon.2023.e15317)<br>[PMID 37113787](https://pubmed.ncbi.nlm.nih.gov/37113787/) | Parameters `step_linear`, `max_crown_step` |
| Ma Y, Li S | 2021 | The optimal orthodontic displacement of clear aligner for mild, moderate and severe periodontal conditions: an in vitro study in a periodontally compromised individual using the finite element model | BMC Oral Health 21(1):109 | [`10.1186/s12903-021-01474-7`](https://doi.org/10.1186/s12903-021-01474-7)<br>[PMID 33691673](https://pubmed.ncbi.nlm.nih.gov/33691673/) | Parameters `perio_step` |
| Yang S, Cheng Y | 2025 | Force-Driven Model for Automated Clear Aligner Staging Design Based on Stepwise Tooth Displacement and Rotation in 3D Space | Bioengineering 12(2):111 | [`10.3390/bioengineering12020111`](https://doi.org/10.3390/bioengineering12020111)<br>[PMID 40001631](https://pubmed.ncbi.nlm.nih.gov/40001631/) | Parameters `max_crown_step`, `collision_tol` |
| Liu Y, Ma Y, Yang L, Zhang C, Wei G, Chen R, et al. | 2025 | A Potential Field Method for Tooth Motion Planning in Orthodontic Treatment | IEEE Trans Vis Comput Graph 31(10):8480-8490 | [`10.1109/TVCG.2025.3567299`](https://doi.org/10.1109/TVCG.2025.3567299)<br>[PMID 40388270](https://pubmed.ncbi.nlm.nih.gov/40388270/) | Parameters `collision_tol` |
| Kravitz ND, Kusnoto B, BeGole E, Obrez A, Agran B | 2009 | How well does Invisalign work? A prospective clinical study evaluating the efficacy of tooth movement with Invisalign | Am J Orthod Dentofacial Orthop 135(1):27-35 | [`10.1016/j.ajodo.2007.05.018`](https://doi.org/10.1016/j.ajodo.2007.05.018)<br>[PMID 19121497](https://pubmed.ncbi.nlm.nih.gov/19121497/) | Parameters `vertical_auto_max` |
| Haouili N, Kravitz ND, Vaid NR, Ferguson DJ, Makki L | 2020 | Has Invisalign improved? A prospective follow-up study on the efficacy of tooth movement with Invisalign | Am J Orthod Dentofacial Orthop 158(3):420-425 | [`10.1016/j.ajodo.2019.12.015`](https://doi.org/10.1016/j.ajodo.2019.12.015)<br>[PMID 32620479](https://pubmed.ncbi.nlm.nih.gov/32620479/) | Parameters `vertical_auto_max` |
| Koletsi D, Iliadi A, Eliades T | 2021 | Predictability of rotational tooth movement with orthodontic aligners comparing software-based and achieved data: A systematic review and meta-analysis of observational studies | J Orthod 48(3):277-287 | [`10.1177/14653125211027266`](https://doi.org/10.1177/14653125211027266)<br>[PMID 34176358](https://pubmed.ncbi.nlm.nih.gov/34176358/) | Evidence base (finding text and report); no parameter cites it directly |
| Kravitz ND, Kusnoto B, Agran B, Viana G | 2008 | Influence of attachments and interproximal reduction on the accuracy of canine rotation with Invisalign | Angle Orthod 78(4):682-687 | [`10.2319/0003-3219(2008)078[0682:IOAAIR]2.0.CO;2`](https://doi.org/10.2319/0003-3219%282008%29078%5B0682:IOAAIR%5D2.0.CO;2)<br>[PMID 18302468](https://pubmed.ncbi.nlm.nih.gov/18302468/) | Evidence base (finding text and report); no parameter cites it directly |
| Rossini G, Parrini S, Castroflorio T, Deregibus A, Debernardi CL | 2015 | Efficacy of clear aligners in controlling orthodontic tooth movement: a systematic review | Angle Orthod 85(5):881-889 | [`10.2319/061614-436.1`](https://doi.org/10.2319/061614-436.1)<br>[PMID 25412265](https://pubmed.ncbi.nlm.nih.gov/25412265/) | Evidence base (finding text and report); no parameter cites it directly |
| Papadimitriou A, Mousoulea S, Gkantidis N, Kloukos D | 2018 | Clinical effectiveness of Invisalign orthodontic treatment: a systematic review | Prog Orthod 19(1):37 | [`10.1186/s40510-018-0235-z`](https://doi.org/10.1186/s40510-018-0235-z)<br>[PMID 30264270](https://pubmed.ncbi.nlm.nih.gov/30264270/) | Evidence base (finding text and report); no parameter cites it directly |
| Palone M, Pignotti A, Morin E, Pancari C, Spedicato GA, Cremonini F, et al. | 2023 | Analysis of overcorrection to be included for planning clear aligner therapy: a retrospective study | Angle Orthod 93(1):11-18 | [`10.2319/052022-371.1`](https://doi.org/10.2319/052022-371.1)<br>[PMID 36223202](https://pubmed.ncbi.nlm.nih.gov/36223202/) | Parameters `overcorrection` |
| Bollen AM, Huang G, King G, Hujoel P, Ma T | 2003 | Activation time and material stiffness of sequential removable orthodontic appliances. Part 1: Ability to complete treatment | Am J Orthod Dentofacial Orthop 124(5):496-501 | [`10.1016/S0889-5406(03)00576-6`](https://doi.org/10.1016/S0889-5406%2803%2900576-6)<br>[PMID 14614415](https://pubmed.ncbi.nlm.nih.gov/14614415/) | Parameters `interval_days` |
| Al-Nadawi M, Kravitz ND, Hansa I, Makki L, Ferguson DJ, Vaid NR | 2021 | Effect of clear aligner wear protocol on the efficacy of tooth movement | Angle Orthod 91(2):157-163 | [`10.2319/071520-630.1`](https://doi.org/10.2319/071520-630.1)<br>[PMID 33296455](https://pubmed.ncbi.nlm.nih.gov/33296455/) | Parameters `interval_days`, `tracking_linear`, `tracking_angular` |
| Timm LH, Farrag G, Baxmann M, Schwendicke F | 2021 | Factors Influencing Patient Compliance during Clear Aligner Therapy: A Retrospective Cohort Study | J Clin Med 10(14):3103 | [`10.3390/jcm10143103`](https://doi.org/10.3390/jcm10143103)<br>[PMID 34300269](https://pubmed.ncbi.nlm.nih.gov/34300269/) | Parameters `wear_hours` |
| Ravera S, Castroflorio T, Garino F, Daher S, Cugliari G, Deregibus A | 2016 | Maxillary molar distalization with aligners in adult patients: a multicenter retrospective study | Prog Orthod 17:12 | [`10.1186/s40510-016-0126-0`](https://doi.org/10.1186/s40510-016-0126-0)<br>[PMID 27041551](https://pubmed.ncbi.nlm.nih.gov/27041551/) | Parameters `seq_overlap`, `distal_predictable` |
| Wang Y, Long H, Zhao Z, Bai D, Han X, Wang J, et al. | 2025 | Expert consensus on the clinical strategies for orthodontic treatment with clear aligners | Int J Oral Sci 17(1):19 | [`10.1038/s41368-025-00350-2`](https://doi.org/10.1038/s41368-025-00350-2)<br>[PMID 40074738](https://pubmed.ncbi.nlm.nih.gov/40074738/) | Parameters `expansion_upper`, `expansion_lower_posterior`, `advance_incisors`, `ipr_surface`, `ipr_enamel_fraction`, `extraction_threshold`, `distal_predictable` |
| Long H, Wu Z, Yan X, et al. | 2020 | An objective system for appraising clear aligner treatment difficulty: clear aligner treatment complexity assessment tool (CAT-CAT) | BMC Oral Health 20(1):312 | [`10.1186/s12903-020-01300-6`](https://doi.org/10.1186/s12903-020-01300-6)<br>[PMID 33167950](https://pubmed.ncbi.nlm.nih.gov/33167950/) | Evidence base (finding text and report); no parameter cites it directly |
| Grunheid T, Loh C, Larson BE | 2017 | How accurate is Invisalign in nonextraction cases? Are predicted tooth positions achieved? | Angle Orthod 87(6):809-815 | [`10.2319/022717-147.1`](https://doi.org/10.2319/022717-147.1)<br>[PMID 28686090](https://pubmed.ncbi.nlm.nih.gov/28686090/) | Parameters `tracking_linear`, `tracking_angular` |

### 1.2 Dental arch form, tooth size and crowding

Arch-form fitting, arch-length limits and case analysis (`dca-algo` diagnosis and setup).

| Authors | Year | Title | Venue | DOI / PMID | Used in `evidence.rs` |
| --- | --- | --- | --- | --- | --- |
| Braun S, Hnat WP, Fender DE, Legan HL | 1998 | The form of the human dental arch | Angle Orthod 68(1):29-36 | [`10.1043/0003-3219(1998)068<0029:TFOTHD>2.3.CO;2`](https://doi.org/10.1043/0003-3219%281998%29068%3C0029:TFOTHD%3E2.3.CO;2) †<br>[PMID 9503132](https://pubmed.ncbi.nlm.nih.gov/9503132/) | Evidence base (finding text and report); no parameter cites it directly |
| AlHarbi S, Alkofide EA, AlMadi A | 2008 | Mathematical analyses of dental arch curvature in normal occlusion | Angle Orthod 78(2):281-287 | [`10.2319/121806-516.1`](https://doi.org/10.2319/121806-516.1)<br>[PMID 18251619](https://pubmed.ncbi.nlm.nih.gov/18251619/) | Evidence base (finding text and report); no parameter cites it directly |
| Noroozi H, Hosseinzadeh Nik T, Saeeda R | 2001 | The dental arch form revisited | Angle Orthod 71(5):386-389 | [`10.1043/0003-3219(2001)071<0386:TDAFR>2.0.CO;2`](https://doi.org/10.1043/0003-3219%282001%29071%3C0386:TDAFR%3E2.0.CO;2) †<br>[PMID 11605873](https://pubmed.ncbi.nlm.nih.gov/11605873/) | Evidence base (finding text and report); no parameter cites it directly |
| Little RM | 1975 | The irregularity index: a quantitative score of mandibular anterior alignment | Am J Orthod 68(5):554-563 | [`10.1016/0002-9416(75)90086-X`](https://doi.org/10.1016/0002-9416%2875%2990086-X)<br>[PMID 1059332](https://pubmed.ncbi.nlm.nih.gov/1059332/) | Evidence base (finding text and report); no parameter cites it directly |
| Bolton WA | 1958 | Disharmony in tooth size and its relation to the analysis and treatment of malocclusion | Angle Orthod 28(3):113-130 | no DOI; not checked online | Evidence base (finding text and report); no parameter cites it directly |
| Germane N, Lindauer SJ, Rubenstein LK, Revere JH, Isaacson RJ | 1991 | Increase in arch perimeter due to orthodontic expansion | Am J Orthod Dentofacial Orthop 100(5):421-427 | [`10.1016/0889-5406(91)70081-7`](https://doi.org/10.1016/0889-5406%2891%2970081-7)<br>[PMID 1815557](https://pubmed.ncbi.nlm.nih.gov/1815557/) | Parameters `advance_incisors` |
| Hnat WP, Braun S, Chinhara A, Legan HL | 2000 | The relationship of arch length to alterations in dental arch width | Am J Orthod Dentofacial Orthop 118(2):184-188 | [`10.1067/mod.2000.105570`](https://doi.org/10.1067/mod.2000.105570)<br>[PMID 10935959](https://pubmed.ncbi.nlm.nih.gov/10935959/) | Evidence base (finding text and report); no parameter cites it directly |
| Burke SP, Silveira AM, Goldsmith LJ, et al. | 1998 | A meta-analysis of mandibular intercanine width in treatment and postretention | Angle Orthod 68(1):53-60 | [`10.1043/0003-3219(1998)068<0053:AMAOMI>2.3.CO;2`](https://doi.org/10.1043/0003-3219%281998%29068%3C0053:AMAOMI%3E2.3.CO;2) †<br>[PMID 9503135](https://pubmed.ncbi.nlm.nih.gov/9503135/) | Parameters `expansion_lower_canine` |
| Houle JP, Piedade L, Todescan R Jr, Pinheiro FH | 2017 | The predictability of transverse changes with Invisalign | Angle Orthod 87(1):19-24 | [`10.2319/122115-875.1`](https://doi.org/10.2319/122115-875.1)<br>[PMID 27304231](https://pubmed.ncbi.nlm.nih.gov/27304231/) | Parameters `expansion_upper` |
| Zhou N, Guo J | 2020 | Efficiency of upper arch expansion with the Invisalign system | Angle Orthod 90(1):23-30 | [`10.2319/022719-151.1`](https://doi.org/10.2319/022719-151.1)<br>[PMID 31368778](https://pubmed.ncbi.nlm.nih.gov/31368778/) | Parameters `expansion_upper` |
| Andrews LF | 1972 | The six keys to normal occlusion | Am J Orthod 62(3):296-309 | [`10.1016/S0002-9416(72)90268-0`](https://doi.org/10.1016/S0002-9416%2872%2990268-0)<br>[PMID 4505873](https://pubmed.ncbi.nlm.nih.gov/4505873/) | Parameters `occlusion_class_i` |
| Casko JS, et al. | 1998 | Objective grading system for dental casts and panoramic radiographs | Am J Orthod Dentofacial Orthop 114(5):589-599 | [`10.1016/S0889-5406(98)70179-9`](https://doi.org/10.1016/S0889-5406%2898%2970179-9)<br>[PMID 9810056](https://pubmed.ncbi.nlm.nih.gov/9810056/) | Parameters `occlusion_bite_warn` |

### 1.3 Periodontal and anatomical limits, biomechanics

Limits on tooth movement and the centre of resistance (`dca-algo` setup, staging and shell).

| Authors | Year | Title | Venue | DOI / PMID | Used in `evidence.rs` |
| --- | --- | --- | --- | --- | --- |
| Yared KF, Zenobio EG, Pacheco W | 2006 | Periodontal status of mandibular central incisors after orthodontic proclination in adults | Am J Orthod Dentofacial Orthop 130(1):6.e1-8 | [`10.1016/j.ajodo.2006.01.015`](https://doi.org/10.1016/j.ajodo.2006.01.015)<br>[PMID 16849063](https://pubmed.ncbi.nlm.nih.gov/16849063/) | Parameters `advance_incisors` |
| Artun J, Krogstad O | 1987 | Periodontal status of mandibular incisors following excessive proclination | Am J Orthod Dentofacial Orthop 91(3):225-232 | [`10.1016/0889-5406(87)90450-1`](https://doi.org/10.1016/0889-5406%2887%2990450-1)<br>[PMID 3469907](https://pubmed.ncbi.nlm.nih.gov/3469907/) | Parameters `advance_incisors` |
| Handelman CS | 1996 | The anterior alveolus: its importance in limiting orthodontic treatment and its influence on the occurrence of iatrogenic sequelae | Angle Orthod 66(2):95-109 | [`10.1043/0003-3219(1996)066<0095:TAAIII>2.3.CO;2`](https://doi.org/10.1043/0003-3219%281996%29066%3C0095:TAAIII%3E2.3.CO;2) †<br>[PMID 8712499](https://pubmed.ncbi.nlm.nih.gov/8712499/) | Parameters `advance_incisors`, `retract_incisors` |
| Poppe M, Bourauel C, Jager A | 2002 | Determination of the elasticity parameters of the human periodontal ligament and the location of the center of resistance of single-rooted teeth | J Orofac Orthop 63(5):358-370 | [`10.1007/s00056-002-0067-8`](https://doi.org/10.1007/s00056-002-0067-8)<br>[PMID 12297965](https://pubmed.ncbi.nlm.nih.gov/12297965/) | Parameters `cres_ratio` |
| Gargiulo AW, Wentz FM, Orban B | 1961 | Dimensions and relations of the dentogingival junction in humans | J Periodontol 32:261-267 | [`10.1902/jop.1961.32.3.261`](https://doi.org/10.1902/jop.1961.32.3.261) | Parameters `margin_to_crest`, `neck_depth` |

### 1.4 Interproximal reduction (IPR)

Enamel thickness and IPR limits (`dca-algo` setup and staging).

| Authors | Year | Title | Venue | DOI / PMID | Used in `evidence.rs` |
| --- | --- | --- | --- | --- | --- |
| Firinciogullari EC, Erdinc AE, Akyalcin S | 2025 | 3-Dimensional Evaluation of Enamel Thickness to Guide Orthodontic Interproximal Reduction: A CBCT-Based Study Across Gender and Ethnicity | Turk J Orthod 38(2):89-96 | [`10.4274/TurkJOrthod.2025.2025.36`](https://doi.org/10.4274/TurkJOrthod.2025.2025.36) | Parameters `ipr_enamel_fraction` |
| Gonzalez-Garcia E, Balut-Chahin N, Rojo-Arce CD, Corona MEJ, Cruz-Hervert LP, Retrouvey JM | 2025 | Assessing Enamel Thickness to Estimate Interproximal Reduction: A CBCT-Based Study | Clin Exp Dent Res 11(1):e70083 | [`10.1002/cre2.70083`](https://doi.org/10.1002/cre2.70083) | Parameters `ipr_site_warning` |
| Zachrisson BU, Nyoygaard L, Mobarak K | 2007 | Dental health assessed more than 10 years after interproximal enamel reduction of mandibular anterior teeth | Am J Orthod Dentofacial Orthop 131(2):162-169 | [`10.1016/j.ajodo.2006.10.001`](https://doi.org/10.1016/j.ajodo.2006.10.001)<br>[PMID 17276856](https://pubmed.ncbi.nlm.nih.gov/17276856/) | Parameters `ipr_surface` |
| De Felice ME, Nucci L, Fiori A, Flores-Mir C, Perillo L, Grassia V | 2020 | Accuracy of interproximal enamel reduction during clear aligner treatment | Prog Orthod 21(1):28 | [`10.1186/s40510-020-00329-1`](https://doi.org/10.1186/s40510-020-00329-1)<br>[PMID 32719906](https://pubmed.ncbi.nlm.nih.gov/32719906/) | Evidence base (finding text and report); no parameter cites it directly |

### 1.5 Trimline, gingival margin and retention

Aligner trim line and margin defaults (`dca-algo` trim).

| Authors | Year | Title | Venue | DOI / PMID | Used in `evidence.rs` |
| --- | --- | --- | --- | --- | --- |
| Elshazly TM, Keilig L, Salvatori D, et al. | 2022 | Effect of trimming line design and edge extension of orthodontic aligners on force transmission: An in vitro study | J Dent 125:104276 | [`10.1016/j.jdent.2022.104276`](https://doi.org/10.1016/j.jdent.2022.104276)<br>[PMID 36055460](https://pubmed.ncbi.nlm.nih.gov/36055460/) | Parameters `trim_extension` |
| Elshazly TM, Salvatori D, Elattar H, et al. | 2023 | Effect of trimming line design and edge extension of orthodontic aligners on force transmission: A 3D finite element study | J Mech Behav Biomed Mater 140:105741 | [`10.1016/j.jmbbm.2023.105741`](https://doi.org/10.1016/j.jmbbm.2023.105741)<br>[PMID 36857974](https://pubmed.ncbi.nlm.nih.gov/36857974/) | Parameters `trim_extension` |
| Elshazly TM, Bourauel C, Aldesoki M, et al. | 2024 | Effect of attachment configuration and trim line design on the force system of orthodontic aligners: A finite element study on the upper central incisor | Orthod Craniofac Res 27(Suppl 2):131-140 | [`10.1111/ocr.12779`](https://doi.org/10.1111/ocr.12779)<br>[PMID 38459802](https://pubmed.ncbi.nlm.nih.gov/38459802/) | Evidence base (finding text and report); no parameter cites it directly |
| Traversa F, Chavanne P, Mah J | 2025 | Biomechanics of clear aligner therapy: Assessing the influence of tooth position and flat trimline height in translational movements | Orthod Craniofac Res 28(1):1-11 | [`10.1111/ocr.12796`](https://doi.org/10.1111/ocr.12796)<br>[PMID 38685814](https://pubmed.ncbi.nlm.nih.gov/38685814/) | Parameters `trim_extension` |
| Cowley DP, Mah J, O'Toole B | 2012 | The effect of gingival-margin design on the retention of thermoformed aligners | J Clin Orthod 46(11):697-702 | [PMID 23395874](https://pubmed.ncbi.nlm.nih.gov/23395874/) | Parameters `trim_extension`, `shell_thickness`, `trim_equator_offset` |
| Nakornnoi T, Srirodjanakul W, Chintavalakorn R, Santiwong P, Sipiyaruk K | 2024 | The biomechanical effects of clear aligner trimline designs and extensions on orthodontic tooth movement: a systematic review | BMC Oral Health 24(1):1523 | [`10.1186/s12903-024-05274-7`](https://doi.org/10.1186/s12903-024-05274-7)<br>[PMID 39707339](https://pubmed.ncbi.nlm.nih.gov/39707339/) | Parameters `trim_equator_offset` |
| Bortoli NA, Picolli Bernd G, Radke Bittencourt H, Spohr AM, Blessmann Weber JB | 2026 | Retention of orthodontic aligners with different gingival margin designs on three-dimensionally printed models representing varying degrees of marginal tissue recession | Korean J Orthod 56(3):200-206 | [`10.4041/kjod25.269`](https://doi.org/10.4041/kjod25.269)<br>[PMID 42045106](https://pubmed.ncbi.nlm.nih.gov/42045106/) | Parameters `trim_equator_offset` |
| Tran TBV, Pham TNC | 2026 | Retentive force of thermoformed and direct 3D-printed clear aligners with different margin designs and attachments: an in vitro study | Front Oral Health 7:1881161 | [`10.3389/froh.2026.1881161`](https://doi.org/10.3389/froh.2026.1881161)<br>[PMID 42488135](https://pubmed.ncbi.nlm.nih.gov/42488135/) | Parameters `trim_equator_offset` |

### 1.6 Attachments, undercuts and path of insertion

Attachment, blockout and survey-line parameters (`dca-algo` shell and blockout).

| Authors | Year | Title | Venue | DOI / PMID | Used in `evidence.rs` |
| --- | --- | --- | --- | --- | --- |
| Dasy H, Dasy A, Asatrian G, Rozsa N, Lee HF, Kwak JH | 2015 | Effects of variable attachment shapes and aligner material on aligner retention | Angle Orthod 85(6):934-940 | [`10.2319/091014-637.1`](https://doi.org/10.2319/091014-637.1)<br>[PMID 26516708](https://pubmed.ncbi.nlm.nih.gov/26516708/) | Parameters `trim_equator_offset` |
| Nucera R, Dolci C, Bellocchio AM, Costa S, Barbera S, Rustico L, et al. | 2022 | Effects of Composite Attachments on Orthodontic Clear Aligners Therapy: A Systematic Review | Materials 15(2):533 | [`10.3390/ma15020533`](https://doi.org/10.3390/ma15020533)<br>[PMID 35057250](https://pubmed.ncbi.nlm.nih.gov/35057250/) | Evidence base (finding text and report); no parameter cites it directly |
| Bezzon OL, Mattos MG, Ribeiro RF | 1997 | Surveying removable partial dentures: the importance of guiding planes and path of insertion for stability | J Prosthet Dent 78(4):412-418 | [`10.1016/s0022-3913(97)70051-9`](https://doi.org/10.1016/s0022-3913%2897%2970051-9)<br>[PMID 9338875](https://pubmed.ncbi.nlm.nih.gov/9338875/) | Parameters `trim_equator_offset`, `insertion_tilt_anterior`, `insertion_tilt_posterior`, `insertion_tilt_neighbour`, `insertion_tilt_common` |
| Wu L, Lu PJ, Wang Y, Ai HJ, Han J | 2009 | The identification of electronic surveying lines on 3-D digital models of dentition defects | Zhonghua Kou Qiang Yi Xue Za Zhi 44(2):117-120 (in cinese) | [PMID 19563048](https://pubmed.ncbi.nlm.nih.gov/19563048/) | Parameters `trim_equator_offset` |

### 1.7 Aligner material, thickness and 3D-printed aligners

Shell thickness, offsets and print-check limits (`dca-algo` shell and export).

| Authors | Year | Title | Venue | DOI / PMID | Used in `evidence.rs` |
| --- | --- | --- | --- | --- | --- |
| Hahn W, Dathe H, Fialka-Fricke J, Fricke-Zech S, Zapf A, Kubein-Meesenburg D, et al. | 2009 | Influence of thermoplastic appliance thickness on the magnitude of force delivered to a maxillary central incisor during tipping | Am J Orthod Dentofacial Orthop 136(1):12.e1-12.e7 | [`10.1016/j.ajodo.2008.12.015`](https://doi.org/10.1016/j.ajodo.2008.12.015)<br>[PMID 19577136](https://pubmed.ncbi.nlm.nih.gov/19577136/) | Parameters `shell_thickness` |
| Kohda N, Iijima M, Muguruma T, Brantley WA, Ahluwalia KS, Mizoguchi I | 2013 | Effects of mechanical properties of thermoplastic materials on the initial force of thermoplastic appliances | Angle Orthod 83(3):476-483 | [`10.2319/052512-432.1`](https://doi.org/10.2319/052512-432.1)<br>[PMID 23035832](https://pubmed.ncbi.nlm.nih.gov/23035832/) | Parameters `shell_thickness` |
| Kwon JS, Lee YK, Lim BS, Lim YK | 2008 | Force delivery properties of thermoplastic orthodontic materials | Am J Orthod Dentofacial Orthop 133(2):228-234 | [`10.1016/j.ajodo.2006.03.034`](https://doi.org/10.1016/j.ajodo.2006.03.034)<br>[PMID 18249289](https://pubmed.ncbi.nlm.nih.gov/18249289/) | Parameters `shell_thickness` |
| Grant J, Foley P, Bankhead B, Miranda G, Adel SM, Kim KB | 2023 | Forces and moments generated by 3D direct printed clear aligners of varying labial and lingual thicknesses during lingual movement of maxillary central incisor: an in vitro study | Prog Orthod 24(1):23 | [`10.1186/s40510-023-00475-2`](https://doi.org/10.1186/s40510-023-00475-2)<br>[PMID 37423974](https://pubmed.ncbi.nlm.nih.gov/37423974/) | Evidence base (finding text and report); no parameter cites it directly |
| Bandic R, Vodanovic K, Vukovic Kekez I, Medvedec Mikic I, Galic I, Kalibovic Govorko D | 2024 | Thickness Variations of Thermoformed and 3D-Printed Clear Aligners | Acta Stomatol Croat 58(2):145-155 | [`10.15644/asc58/2/4`](https://doi.org/10.15644/asc58/2/4)<br>[PMID 39036327](https://pubmed.ncbi.nlm.nih.gov/39036327/) | Parameters `shell_thickness` |
| Bucci R, Rongo R, Levate C, Michelotti A, Barone S, Razionale AV, et al. | 2019 | Thickness of orthodontic clear aligners after thermoforming and after 10 days of intraoral exposure: a prospective clinical study | Prog Orthod 20(1):36 | [`10.1186/s40510-019-0289-6`](https://doi.org/10.1186/s40510-019-0289-6)<br>[PMID 31495908](https://pubmed.ncbi.nlm.nih.gov/31495908/) | Parameters `shell_thickness` |
| Edelmann A, English JD, Chen SJ, Kasper FK | 2020 | Analysis of the thickness of 3-dimensional-printed orthodontic aligners | Am J Orthod Dentofacial Orthop 158(5):e91-e98 | [`10.1016/j.ajodo.2020.07.029`](https://doi.org/10.1016/j.ajodo.2020.07.029)<br>[PMID 33131570](https://pubmed.ncbi.nlm.nih.gov/33131570/) | Parameters `shell_thickness` |
| Koenig N, Choi JY, McCray J, Hayes A, Schneider P, Kim KB | 2022 | Comparison of dimensional accuracy between direct-printed and thermoformed aligners | Korean J Orthod 52(4):249-257 | [`10.4041/kjod21.269`](https://doi.org/10.4041/kjod21.269)<br>[PMID 35466087](https://pubmed.ncbi.nlm.nih.gov/35466087/) | Parameters `shell_thickness` |

### 1.8 Occlusion and bite registration

Bite registration, occlusal contacts and the rules for accepting a bite scan (`dca-algo` occlusion and bite).

| Authors | Year | Title | Venue | DOI / PMID | Used in `evidence.rs` |
| --- | --- | --- | --- | --- | --- |
| Solaberrieta E, Otegi JR, Goicoechea N, Brizuela A, Pradies G | 2015 | Comparison of a conventional and virtual occlusal record | J Prosthet Dent 114(1):92-97 | [`10.1016/j.prosdent.2015.01.009`](https://doi.org/10.1016/j.prosdent.2015.01.009) | Evidence base (finding text and report); no parameter cites it directly |
| Solaberrieta E, Arias A, Brizuela A, Garikano X, Pradies G | 2016 | Determining the requirements, section quantity, and dimension of the virtual occlusal record | J Prosthet Dent 115(1):52-56 | [`10.1016/j.prosdent.2015.06.013`](https://doi.org/10.1016/j.prosdent.2015.06.013) | Parameters `bite_min_area` |
| Solaberrieta E, Garmendia A, Brizuela A, Otegi JR, Pradies G, Szentpetery A | 2016 | Intraoral Digital Impressions for Virtual Occlusal Records: Section Quantity and Dimensions | BioMed Res Int 2016:7173824 | [`10.1155/2016/7173824`](https://doi.org/10.1155/2016/7173824) | Parameters `bite_min_teeth` |
| Revilla-Leon M, Alonso Perez-Barquero J, Zubizarreta-Macho A, Barmak AB, Att W, Kois JC | 2023 | Influence of the Number of Teeth and Location of the Virtual Occlusal Record on the Accuracy of the Maxillo-Mandibular Relationship Obtained by Using An Intraoral Scanner | J Prosthodont 32(3):253-258 | [`10.1111/jopr.13526`](https://doi.org/10.1111/jopr.13526) | Parameters `bite_min_teeth`, `bite_teeth` |
| Revilla-Leon M, Barmak AB, Tohme H, Yilmaz B, Kois JC, Gomez-Polo M | 2023 | Factors that influence the accuracy of maxillomandibular relationship at maximum intercuspation acquired by using intraoral scanners: A systematic review | J Dent 138:104718 | [`10.1016/j.jdent.2023.104718`](https://doi.org/10.1016/j.jdent.2023.104718) | Parameters `bite_teeth` |
| Revilla-Leon M, Gomez-Polo M, Zeitler JM, Barmak AB, Kois JC, Perez-Barquero JA | 2024 | Does the available interocclusal space influence the accuracy of the maxillomandibular relationship captured with an intraoral scanner? | J Prosthet Dent 132(2):435-440 | [`10.1016/j.prosdent.2022.09.004`](https://doi.org/10.1016/j.prosdent.2022.09.004) | Evidence base (finding text and report); no parameter cites it directly |
| Revilla-Leon M, Gomez-Polo M, Barmak AB, Kois JC, Yilmaz B, Alonso Perez-Barquero J | 2024 | Influence of occlusal collision corrections completed by two intraoral scanners or a dental design program on the accuracy of the maxillomandibular relationship | J Prosthet Dent 132(1):191-203 | [`10.1016/j.prosdent.2023.05.015`](https://doi.org/10.1016/j.prosdent.2023.05.015) | Evidence base (finding text and report); no parameter cites it directly |
| Mei J, Ma L, Chao J, Liu F, Shen J | 2022 | Three-dimensional analysis of the outcome of different scanning strategies in virtual interocclusal registration | J Adv Prosthodont 14(6):369-378 | [`10.4047/jap.2022.14.6.369`](https://doi.org/10.4047/jap.2022.14.6.369) | Parameters `bite_agreement` |
| Iwauchi Y, Tanaka S, Kamimura-Sugimura E, Baba K | 2022 | Clinical evaluation of the precision of interocclusal registration by using digital and conventional techniques | J Prosthet Dent 128(4):611-617 | [`10.1016/j.prosdent.2021.01.021`](https://doi.org/10.1016/j.prosdent.2021.01.021) | Parameters `bite_inlier`, `bite_rms_good` |
| Koshiishi Y, Tanaka S, Iwauchi Y, Baba K | 2024 | Impact of scanning range and image count on the precision of digitally recorded intermaxillary relationships in interocclusal record using intraoral scanner | J Oral Sci 66(2):111-115 | [`10.2334/josnusd.23-0379`](https://doi.org/10.2334/josnusd.23-0379) | Parameters `bite_inlier`, `bite_rms_good` |
| Garikano X, Amezua X, Iturrate M, Solaberrieta E | 2024 | Evaluation of repeatability of different alignment methods to obtain digital interocclusal records: An in vitro study | J Prosthet Dent 131(4):709-717 | [`10.1016/j.prosdent.2022.07.014`](https://doi.org/10.1016/j.prosdent.2022.07.014) | Parameters `bite_inlier` |
| Kakali L, Halazonetis DJ | 2023 | A novel method for testing accuracy of bite registration using intraoral scanners | Korean J Orthod 53(4):254-263 | [`10.4041/kjod22.199`](https://doi.org/10.4041/kjod22.199) | Parameters `bite_rms_good`, `bite_rms_max`, `bite_agreement` |
| Wong KY, Esguerra RJ, Chia VAP, Tan YH, Tan KBC | 2018 | Three-Dimensional Accuracy of Digital Static Interocclusal Registration by Three Intraoral Scanner Systems | J Prosthodont 27(2):120-128 | [`10.1111/jopr.12714`](https://doi.org/10.1111/jopr.12714) | Parameters `bite_rms_max`, `bite_penetration_max` |
| Beck F, Lettner S, Zupancic Cepic L, Schedle A | 2023 | Comparison of Virtual Intersection and Occlusal Contacts between Intraoral and Laboratory Scans: An In-Vivo Study | J Clin Med 12(3):996 | [`10.3390/jcm12030996`](https://doi.org/10.3390/jcm12030996) | Parameters `bite_gap_warn`, `contact_map_contact` |
| Zhao X, Tu Y, Ding Q, Zhang L | 2026 | Effect of a digital bite registration method considering physiological tooth displacement on virtual occlusion: A self-controlled clinical trial | J Prosthodont (online) | [`10.1111/jopr.70162`](https://doi.org/10.1111/jopr.70162) | Parameters `bite_penetration_max`, `bite_penetration_warn` |
| Lee H, Cha J, Chun YS, Kim M | 2018 | Comparison of the occlusal contact area of virtual models and actual models: a comparative in vitro study on Class I and Class II malocclusion models | BMC Oral Health 18(1):109 | [`10.1186/s12903-018-0566-7`](https://doi.org/10.1186/s12903-018-0566-7) | Parameters `bite_gap_warn`, `contact_map_contact` |
| Edher F, Hannam AG, Tobias DL, Wyatt CCL | 2018 | The accuracy of virtual interocclusal registration during intraoral scanning | J Prosthet Dent 120(6):904-912 | [`10.1016/j.prosdent.2018.01.024`](https://doi.org/10.1016/j.prosdent.2018.01.024) | Evidence base (finding text and report); no parameter cites it directly |
| Popa AD, Vladutu DE, Turcu AA, Tartea DA, Ionescu M, Paunescu C, et al. | 2024 | Aspects of Occlusal Recordings Performed with the T-Scan System and with the Medit Intraoral Scanner | Diagnostics 14(13):1457 | [`10.3390/diagnostics14131457`](https://doi.org/10.3390/diagnostics14131457) | Parameters `bite_penetration_warn` |
| Vladutu DE, Mercut R, Varut MC, Stefarta A, Mercut V, Radoi AM, et al. | 2025 | Assessment of Occlusal Contacts Recorded with the Medit Intraoral Scanner vs. Exocad Software | J Clin Med 14(20):7378 | [`10.3390/jcm14207378`](https://doi.org/10.3390/jcm14207378) | Evidence base (finding text and report); no parameter cites it directly |
| Utt TW, Meyers CE, Wierzba TF, Hondrum SO | 1995 | A three-dimensional comparison of condylar position changes between centric relation and centric occlusion using the mandibular position indicator | Am J Orthod Dentofacial Orthop 107(3):298-308 | [`10.1016/S0889-5406(95)70146-X`](https://doi.org/10.1016/S0889-5406%2895%2970146-X) | Evidence base (finding text and report); no parameter cites it directly |
| Wriedt S, Schmidtmann I, Niemann M, Wehrbein H | 2013 | Digital 3D image of bimaxillary casts connected by a vestibular scan | J Orofac Orthop 74(4):309-318 | [`10.1007/s00056-013-0152-1`](https://doi.org/10.1007/s00056-013-0152-1) | Evidence base (finding text and report); no parameter cites it directly |
| Auskalnis L, Akulauskas M, Osnes C, Revilla-Leon M, Kernen-Gintaute A, Rutkunas V | 2024 | Trueness of maxillomandibular relationship in 3D-printed and conventional casts | J Dent 148:105044 | [`10.1016/j.jdent.2024.105044`](https://doi.org/10.1016/j.jdent.2024.105044) | Evidence base (finding text and report); no parameter cites it directly |

### 1.9 Books and glossary

Textbooks and the prosthodontic glossary cited next to the parameters.

| Authors | Year | Title | Venue | DOI / PMID | Used in `evidence.rs` |
| --- | --- | --- | --- | --- | --- |
| Nelson SJ | 2019 | Wheeler's Dental Anatomy, Physiology and Occlusion | Elsevier, St. Louis | no DOI; not checked online | Parameters `occlusion_class_i`, `bite_tooth_area` |
| Proffit WR, Fields HW, Larson BE, Sarver DM | 2018 | Contemporary Orthodontics, 6th ed. | Elsevier, Philadelphia (ISBN 9780323543873) | no DOI; not checked online | Parameters `occlusion_overjet`, `occlusion_class_i` |
| Okeson JP | 2019 | Management of Temporomandibular Disorders and Occlusion, 8th ed. | Elsevier, St. Louis (ISBN 9780323582100) | no DOI; not checked online | Evidence base (finding text and report); no parameter cites it directly |
| Timoshenko SP, Woinowsky-Krieger S | 1959 | Theory of Plates and Shells, 2nd ed. | McGraw-Hill, New York (ISBN 9780070647794) | no DOI; not checked online | Parameters `shell_thickness` |
| The Academy of Prosthodontics | 2017 | The Glossary of Prosthodontic Terms: Ninth Edition | J Prosthet Dent 117(5S):e1-e105 | [`10.1016/j.prosdent.2016.12.001`](https://doi.org/10.1016/j.prosdent.2016.12.001)<br>[PMID 28418832](https://pubmed.ncbi.nlm.nih.gov/28418832/) | Parameters `trim_equator_offset`, `insertion_tilt_anterior`, `insertion_tilt_posterior`, `insertion_tilt_neighbour`, `insertion_tilt_common` |

### 1.10 Intraoral scanner vendor manuals

Scanning protocols of other scanners, used to set bite-scan guidance. Vendor documents, no DOI.

| Authors | Year | Title | Venue | DOI / PMID | Used in `evidence.rs` |
| --- | --- | --- | --- | --- | --- |
| 3Shape A/S | 2013 | TRIOS User Manual (TRIOS-2013-1-1.2.1.1-B-EN) | 3Shape, Copenaghen | no DOI; not checked online | Parameters `bite_teeth` |
| 3Shape A/S | 2018 | TRIOS info pack: Bite Alignment (v1.1) | 3Shape, Copenaghen | no DOI; not checked online | Parameters `bite_penetration_warn`, `bite_gap_warn` |
| Dentsply Sirona | 2019 | Connect SW 5.1.x Operator's Manual | Dentsply Sirona, Bensheim | no DOI; not checked online | Parameters `contact_map_contact` |
| Align Technology | 2020 | iTero Full-Arch Scanning Guide (MKT-0004794 Rev A); iTero Element 5D User Manual | Align Technology, San Jose | no DOI; not checked online | Parameters `bite_agreement` |

## 2. Geometry algorithms

Part of the same bibliography (`evidence.rs`), grouped here by the algorithm they support.

### 2.1 Registration (ICP) and rigid alignment

Weighted Kabsch, trimmed ICP and point-to-plane ICP: core `dc-geom/src/icp.rs`; bite and scan registration in `dca-algo`.

| Authors | Year | Title | Venue | DOI / PMID | Used in `evidence.rs` |
| --- | --- | --- | --- | --- | --- |
| Besl PJ, McKay ND | 1992 | A method for registration of 3-D shapes | IEEE Trans Pattern Anal Mach Intell 14(2):239-256 | [`10.1109/34.121791`](https://doi.org/10.1109/34.121791) | Evidence base (finding text and report); no parameter cites it directly |
| Chen Y, Medioni G | 1992 | Object modelling by registration of multiple range images | Image Vis Comput 10(3):145-155 | [`10.1016/0262-8856(92)90066-C`](https://doi.org/10.1016/0262-8856%2892%2990066-C) | Evidence base (finding text and report); no parameter cites it directly |
| Kabsch W | 1976 | A solution for the best rotation to relate two sets of vectors | Acta Crystallogr A 32(5):922-923 | [`10.1107/S0567739476001873`](https://doi.org/10.1107/S0567739476001873) | Evidence base (finding text and report); no parameter cites it directly |
| Rusinkiewicz S, Levoy M | 2001 | Efficient variants of the ICP algorithm | Proc. 3rd Int Conf 3-D Digital Imaging and Modeling (3DIM):145-152 | [`10.1109/IM.2001.924423`](https://doi.org/10.1109/IM.2001.924423) | Evidence base (finding text and report); no parameter cites it directly |
| Chetverikov D, Svirko D, Stepanov D, Krsek P | 2002 | The Trimmed Iterative Closest Point algorithm | Proc. 16th Int Conf Pattern Recognition 3:545-548 | [`10.1109/ICPR.2002.1047997`](https://doi.org/10.1109/ICPR.2002.1047997) | Evidence base (finding text and report); no parameter cites it directly |
| Chetverikov D, Stepanov D, Krsek P | 2005 | Robust Euclidean alignment of 3D point sets: the trimmed iterative closest point algorithm | Image Vis Comput 23(3):299-309 | [`10.1016/j.imavis.2004.05.007`](https://doi.org/10.1016/j.imavis.2004.05.007) | Parameters `bite_coherence` |

### 2.2 Tooth segmentation

Random-walk and harmonic-field tooth segmentation: `dca-algo/src/segmentation.rs`, `segmentation/graph.rs`, `manual/fill.rs`.

| Authors | Year | Title | Venue | DOI / PMID | Used in `evidence.rs` |
| --- | --- | --- | --- | --- | --- |
| Lai YK, Hu SM, Martin RR, Rosin PL | 2009 | Rapid and effective segmentation of 3D models using random walks | Comput Aided Geom Des 26(6):665-679 | [`10.1016/j.cagd.2008.09.007`](https://doi.org/10.1016/j.cagd.2008.09.007) | Parameters `rw_eta_convex`, `rw_sigma`, `rw_faces` |
| Grady L | 2006 | Random walks for image segmentation | IEEE Trans Pattern Anal Mach Intell 28(11):1768-1783 | [`10.1109/TPAMI.2006.233`](https://doi.org/10.1109/TPAMI.2006.233) | Evidence base (finding text and report); no parameter cites it directly |
| Zou BJ, Liu SJ, Liao SH, et al. | 2015 | Interactive tooth partition of dental mesh base on tooth-target harmonic field | Comput Biol Med 56:132-144 | [`10.1016/j.compbiomed.2014.10.013`](https://doi.org/10.1016/j.compbiomed.2014.10.013)<br>[PMID 25464355](https://pubmed.ncbi.nlm.nih.gov/25464355/) | Evidence base (finding text and report); no parameter cites it directly |
| Liao SH, Liu SJ, Zou BJ, et al. | 2015 | Automatic Tooth Segmentation of Dental Mesh Based on Harmonic Fields | Biomed Res Int 2015:187173 | [`10.1155/2015/187173`](https://doi.org/10.1155/2015/187173)<br>[PMID 26413507](https://pubmed.ncbi.nlm.nih.gov/26413507/) | Evidence base (finding text and report); no parameter cites it directly |

### 2.3 Interpolation, deformation and mesh editing

Weights and fills used by the setup, shell and stamping stages (`dca-algo`).

| Authors | Year | Title | Venue | DOI / PMID | Used in `evidence.rs` |
| --- | --- | --- | --- | --- | --- |
| Shepard D | 1968 | A two-dimensional interpolation function for irregularly-spaced data | Proc. 23rd ACM National Conference:517-524 | [`10.1145/800186.810616`](https://doi.org/10.1145/800186.810616) | Evidence base (finding text and report); no parameter cites it directly |
| Wendland H | 1995 | Piecewise polynomial, positive definite and compactly supported radial functions of minimal degree | Adv Comput Math 4:389-396 | [`10.1007/BF02123482`](https://doi.org/10.1007/BF02123482) | Evidence base (finding text and report); no parameter cites it directly |
| Kobbelt L, Campagna S, Vorsatz J, Seidel HP | 1998 | Interactive multi-resolution modeling on arbitrary meshes | Proc. SIGGRAPH 98:105-114 | [`10.1145/280814.280831`](https://doi.org/10.1145/280814.280831) | Evidence base (finding text and report); no parameter cites it directly |
| Joshi P, Meyer M, DeRose T, Green B, Sanocki T | 2007 | Harmonic coordinates for character articulation | ACM Trans Graph 26(3):71 | [`10.1145/1276377.1276466`](https://doi.org/10.1145/1276377.1276466) | Evidence base (finding text and report); no parameter cites it directly |

### 2.4 Mesh repair and volumes

Hole filling, sparse volumes (SDF) and mesh checks: core `dc-geom/src/holefill.rs`, `sdf.rs`; `dca-algo` shell and trim.

| Authors | Year | Title | Venue | DOI / PMID | Used in `evidence.rs` |
| --- | --- | --- | --- | --- | --- |
| Liepa P | 2003 | Filling holes in meshes | Eurographics Symposium on Geometry Processing:200-206 | [`10.2312/SGP/SGP03/200-206`](https://doi.org/10.2312/SGP/SGP03/200-206) ‡ | Evidence base (finding text and report); no parameter cites it directly |
| Museth K | 2013 | VDB: High-resolution sparse volumes with dynamic topology | ACM Trans Graph 32(3):27 | [`10.1145/2487228.2487235`](https://doi.org/10.1145/2487228.2487235) | Evidence base (finding text and report); no parameter cites it directly |
| Szilvasi-Nagy M, Matyasi G | 2003 | Analysis of STL files | Math Comput Model 38(7-9):945-960 | [`10.1016/S0895-7177(03)90079-3`](https://doi.org/10.1016/S0895-7177%2803%2990079-3) | Evidence base (finding text and report); no parameter cites it directly |
| Moller T | 1997 | A fast triangle-triangle intersection test | J Graph Tools 2(2):25-30 | [`10.1080/10867651.1997.10487472`](https://doi.org/10.1080/10867651.1997.10487472) | Evidence base (finding text and report); no parameter cites it directly |

### 2.5 Algorithms cited in code comments

These papers are named in comments of `dentalcraft-core` and `dentalcraft-aligners`, not in `evidence.rs`. All DOIs were checked in Crossref on 2026-11-21 (title, first authors, year and pages) except where noted.

| Authors | Year | Title | Venue | DOI / URL | Used in |
| --- | --- | --- | --- | --- | --- |
| Garland M, Heckbert PS | 1997 | Surface simplification using quadric error metrics | SIGGRAPH '97: Proc. 24th Annual Conf. on Computer Graphics and Interactive Techniques, 209-216 | [`10.1145/258734.258849`](https://doi.org/10.1145/258734.258849) | core `dc-geom/src/qem.rs` (mesh decimation) |
| Dey TK, Edelsbrunner H, Guha S, Nekhayev DV | 1999 | Topology preserving edge contraction | Publications de l'Institut Mathématique (Beograd) 66(80):23-45 | No DOI. Record: [EuDML 256270](https://eudml.org/doc/256270) (confirmed 2026-11-21) | core `dc-geom/src/qem.rs` (edge-collapse validity test) |
| Hoppe H, DeRose T, Duchamp T, McDonald J, Stuetzle W | 1992 | Surface reconstruction from unorganized points | SIGGRAPH '92: Proc. 19th Annual Conf. on Computer Graphics and Interactive Techniques, 71-78 | [`10.1145/133994.134011`](https://doi.org/10.1145/133994.134011) | core `dc-geom/src/meshing.rs`, `cloud.rs` |
| Zheng Y, Fu H, Au OK-C, Tai C-L | 2011 | Bilateral normal filtering for mesh denoising | IEEE Trans Vis Comput Graph 17(10):1521-1530 | [`10.1109/TVCG.2010.264`](https://doi.org/10.1109/TVCG.2010.264) | core `dc-geom/src/denoise.rs` |
| Sun X, Rosin PL, Martin RR, Langbein FC | 2007 | Fast and effective feature-preserving mesh denoising | IEEE Trans Vis Comput Graph 13(5):925-938 | [`10.1109/TVCG.2007.1065`](https://doi.org/10.1109/TVCG.2007.1065) | core `dc-geom/src/denoise.rs` |
| Pinkall U, Polthier K | 1993 | Computing discrete minimal surfaces and their conjugates | Experimental Mathematics 2(1):15-36 | [`10.1080/10586458.1993.10504266`](https://doi.org/10.1080/10586458.1993.10504266) | core `dc-geom/src/cotan.rs` (cotangent Laplacian) |
| Umeyama S | 1991 | Least-squares estimation of transformation parameters between two point patterns | IEEE Trans Pattern Anal Mach Intell 13(4):376-380 | [`10.1109/34.88573`](https://doi.org/10.1109/34.88573) | core `dc-geom/src/icp.rs` |
| Gelfand N, Ikemoto L, Rusinkiewicz S, Levoy M | 2003 | Geometrically stable sampling for the ICP algorithm | Proc. 4th Int. Conf. on 3-D Digital Imaging and Modeling (3DIM 2003), 260-267 | [`10.1109/IM.2003.1240258`](https://doi.org/10.1109/IM.2003.1240258); [PDF](https://graphics.stanford.edu/papers/stabicp/stabicp.pdf) | core `dc-geom/src/icp.rs`; `docs/scanner/turntable-scanning-research.md` |
| Taubin G | 1995 | A signal processing approach to fair surface design | SIGGRAPH '95: Proc. 22nd Annual Conf. on Computer Graphics and Interactive Techniques, 351-358 | [`10.1145/218380.218473`](https://doi.org/10.1145/218380.218473) | core `dc-geom/src/repair.rs`, `dc-scanner/src/editor.rs` (named in comments) |
| Lorensen WE, Cline HE | 1987 | Marching cubes: a high resolution 3D surface construction algorithm | SIGGRAPH '87: Proc. 14th Annual Conf. on Computer Graphics and Interactive Techniques, 163-169 | [`10.1145/37401.37422`](https://doi.org/10.1145/37401.37422) | core `dc-geom/src/mc.rs`, `meshing.rs`, `tsdf.rs`, `sdf/mesher.rs` (named in comments) |
| Möller T, Trumbore B | 1997 | Fast, minimum storage ray-triangle intersection | Journal of Graphics Tools 2(1):21-28 | [`10.1080/10867651.1997.10487468`](https://doi.org/10.1080/10867651.1997.10487468) | core `dc-geom/src/bvh.rs` (named in a comment) |
| Newcombe RA, Izadi S, Hilliges O, et al. | 2011 | KinectFusion: real-time dense surface mapping and tracking | 10th IEEE Int. Symp. on Mixed and Augmented Reality (ISMAR 2011), 127-136 | [`10.1109/ISMAR.2011.6092378`](https://doi.org/10.1109/ISMAR.2011.6092378); [PDF](http://www.doc.ic.ac.uk/~ajd/Publications/newcombe_etal_ismar2011.pdf) | core `dc-scanner/src/tracking.rs`; `docs/scanner/turntable-scanning-research.md` |

Also used: OpenVDB `meshToLevelSet` (Museth 2013, section 2.4) in core `dc-geom/src/sdf/` and aligners `shell.rs`, `trim/holes.rs`. The Kabsch, Besl-McKay, Chen-Medioni, Rusinkiewicz-Levoy, Liepa, Lai, Grady, Joshi, Kobbelt, Shepard and Wendland papers of section 2.1 to 2.4 are cited at the same places in code.

## 3. Scanner and turntable

Research notes: `docs/scanner/turntable-scanning-research.md` and `docs/scanner/mini2-capabilities.md`. Code: `dentalcraft-core` crates `dc-scanner`, `dc-turntable`, `dc-ble`.

### 3.1 Papers and software for turntable scanning and registration

| Source | Year | Title / what | Venue | DOI / URL | Used in |
| --- | --- | --- | --- | --- | --- |
| Pang X, Lau RWH, Song Z, Li Y, He S | 2016 (preprint 2014) | A tool-free calibration method for turntable-based 3D scanning systems | IEEE Computer Graphics and Applications 36(1):52-61 | [`10.1109/MCG.2014.83`](https://doi.org/10.1109/MCG.2014.83); [PDF](https://www.cs.cityu.edu.hk/~rynson/papers/cga14.pdf) | Turntable axis calibration design (`turntable.calibrate`) |
| Bisogni L, Mollaiyan R, Pettinari M, Neri P, Gabiccini M | 2020 | Automatic calibration of a two-axis rotary table for 3D scanning purposes | Sensors 20(24):7107 | [`10.3390/s20247107`](https://doi.org/10.3390/s20247107); [PMC7764672](https://pmc.ncbi.nlm.nih.gov/articles/PMC7764672) | Dual-axis (tilt) calibration design |
| Park J, Zhou Q-Y, Koltun V | 2017 | Colored point cloud registration revisited | Proc. IEEE Int. Conf. on Computer Vision (ICCV), 143-152 | [`10.1109/ICCV.2017.25`](https://doi.org/10.1109/ICCV.2017.25); [Open3D tutorial](https://www.open3d.org/docs/release/tutorial/pipelines/colored_pointcloud_registration.html) | Reviewed for pose refinement; not copied |
| Choi S, Zhou Q-Y, Koltun V | 2015 | Robust reconstruction of indoor scenes | Proc. IEEE Conf. on Computer Vision and Pattern Recognition (CVPR), 5556-5565 | [`10.1109/CVPR.2015.7299195`](https://doi.org/10.1109/CVPR.2015.7299195); [Open3D multiway registration](https://www.open3d.org/docs/release/tutorial/pipelines/multiway_registration.html) | Loop-closure and multiway registration design |
| Whelan T, Leutenegger S, Salas-Moreno RF, Glocker B, Davison AJ | 2015 | ElasticFusion: dense SLAM without a pose graph | Robotics: Science and Systems XI | [`10.15607/RSS.2015.XI.001`](https://doi.org/10.15607/RSS.2015.XI.001); [PDF](https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/dyson-robotics-lab/twhelan_etal_rss2015.pdf) | Reviewed in the turntable research note |
| Prisacariu VA, Kähler O, Golodetz S, Sapienza M, Cavallari T, Torr PHS, Murray DW | 2017 | InfiniTAM v3: a framework for large-scale 3D reconstruction with loop closure | arXiv:1708.00783 | [arXiv](https://arxiv.org/abs/1708.00783); [code](https://github.com/victorprad/InfiniTAM) | Reviewed in the turntable research note |
| Open3D documentation (global registration, dense SLAM) | n/a | Tutorials | Open3D project | [global registration](https://www.open3d.org/docs/release/tutorial/pipelines/global_registration.html); [dense SLAM](https://www.open3d.org/docs/release/tutorial/t_reconstruction_system/dense_slam.html) | Reviewed; no code used |
| bqlabs | n/a | Horus / Ciclop (`platform_extrinsics.py`, `point_cloud_roi.py`), GPL-2.0 | GitHub | [github.com/bqlabs/horus](https://github.com/bqlabs/horus) | Only the idea (platform plane plus circle fit) is described. No Horus code is used. |
| mp3guy | n/a | ICPCUDA README | GitHub | [github.com/mp3guy/icpcuda](https://github.com/mp3guy/icpcuda) | Reviewed in the turntable research note |

### 3.2 Revopoint documents and community projects

| Source | Type | URL | Used in |
| --- | --- | --- | --- |
| Revo Scan Android user guide v5.4.0 (2025-03-12) | Vendor manual | [PDF](https://dl.revopoint3d.com/document/soft/revoscan-android-userguide-en-v5.4.0-20250312.pdf) | Scanner and turntable behaviour (`docs/scanner/`) |
| Revopoint MINI 2 user manual (FCC ID 2AY7J) | Vendor manual | [PDF](https://fccid.co/api/files/s1/2ay7j_mini2_usersmanual_6991696_fe244cf403.pdf) | `docs/scanner/mini2-capabilities.md` |
| Revopoint MINI product page and support article 8707367541147 | Vendor web pages | [product](https://www.revopoint3d.com/products/industry-3d-scanner-mini); [support](https://support.revopoint3d.com/hc/en-us/articles/8707367541147) | `docs/scanner/mini2-capabilities.md` |
| Revopoint blog: dual-axis turntable and app tips | Vendor blog | [link](https://global.revopoint3d.com/blogs/blog/dual-axis-turntable-and-app-tips) | `docs/scanner/turntable-scanning-research.md` |
| Revopoint forum threads 24149, 23982, 38719 | Forum | [24149](https://forum.revopoint3d.com/t/feature-request-turntable-single-frame/24149); [23982](https://forum.revopoint3d.com/t/openscantable-for-mini/23982); [38719](https://forum.revopoint3d.com/t/mini2-view-angle-and-best-working-distance/38719) | Field of view, working distance, turntable behaviour |
| Revopoint `3DCamera` SDK v3.2.229 (headers `h/system.h`, `camera.h`, `frame.h`, `hpp/Types.hpp`) | Vendor SDK, proprietary | Not redistributed | core `dc-scanner/src/revopoint_sdk.rs`: loaded at run time from a path the user sets; the C API is declared by hand. The user needs the right to use the SDK. |
| BR1ZB3AR, All3DScan (`RE_NOTES.md`) | Community reverse engineering | [GitHub](https://github.com/BR1ZB3AR/All3DScan) | MINI 2 USB extension-unit notes: core `revopoint_usb/factory.rs`, `xu.rs`. Facts only, no code copied. |
| HazenBabcock, revopoint-python | Community project | [GitHub](https://github.com/HazenBabcock/revopoint-python) | `docs/scanner/mini2-capabilities.md` |
| TamedTornado, revopoint-pop3-linux-wifi | Community project | [GitHub](https://github.com/TamedTornado/revopoint-pop3-linux-wifi) | `docs/scanner/mini2-capabilities.md` |
| vybesforge, revopointinspire2-forge | Community project | [GitHub](https://github.com/vybesforge/revopointinspire2-forge) | `docs/scanner/mini2-capabilities.md` |
| opensourcemanufacturing, Revopoint-Dual-Turntable | Community protocol notes | [GitHub](https://github.com/opensourcemanufacturing/Revopoint-Dual-Turntable) | Turntable Bluetooth LE protocol: core `dc-turntable/src/revopoint.rs`. Facts only. |
| SphaeroX, Revopoint-Dual-Axis-Turntable | Community protocol notes | [GitHub](https://github.com/SphaeroX/Revopoint-Dual-Axis-Turntable) | Same |
| aderusha, ha-revopoint-turntable | Community project | [GitHub](https://github.com/aderusha/ha-revopoint-turntable) | Same |

The licences of the community projects were not re-read for this file. DentalCraft took protocol facts only (offsets, command numbers, behaviour). Revopoint is a trademark of its owner; DentalCraft is not affiliated with it.

## 4. Datasets

| Dataset | Reference | Licence | Used in |
| --- | --- | --- | --- |
| Teeth3DS+ | Ben-Hamadou A, Neifar N, Rekik A, Smaoui O, Bouzguenda F, Pujades S, et al. *Teeth3DS+: an extended benchmark for intraoral 3D scans analysis.* arXiv:2210.06094, 2022. Basis of the MICCAI 3DTeethSeg'22 and 3DTeethLand'24 challenges. [arXiv](https://arxiv.org/abs/2210.06094); data at [osf.io/xctdy](https://osf.io/xctdy/) | CC BY-NC-ND 4.0, as stated in the documents of the Blender add-on (not re-checked) | Validation only, through the environment variable `DC_TEETH3DS` or `DC_REAL_SCANS`. **Never committed.** Aggregate measurements from 4 patients are quoted in `dca-algo/src/evidence.rs` (bite-registration finding). Real-scan tests in `dentalcraft-aligners` read the scans from outside the repository and keep only rounded counts. |
| Synthetic demo arches | Generated by the `demo.generate` function of the Blender add-on (seed 7, voxel 0.35 mm) | Own work | `dentalcraft-aligners/golden/fixtures/` and `crates/dca-algo/tests/fixtures/`. Synthetic data only. |

## 5. Standards, regulations and protocols

### 5.1 Dental, medical-device and data-protection texts

The regulatory texts below are the basis of the "not a medical device" stance and of the regulatory documents carried over from the Blender add-on. DentalCraft does not claim conformity with any of them.

| Item | Where it is used |
| --- | --- |
| ISO 3950, FDI two-digit tooth notation (edition in force not checked) | core `dc-case/src/fdi.rs` |
| Regulation (EU) 2017/745 on medical devices (MDR), [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2017/745/oj) | Disclaimers in `dentalcraft-app` and the website; `dca-algo/src/export/text.rs`; the add-on's regulatory classification |
| Regulation (EU) 2016/679 (GDPR), art. 9, [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | App privacy texts (`dc-app` Fluent files), diagnostics design, pseudonymised case codes |
| Commission Implementing Regulation (EU) 2021/2226 (electronic instructions for use) | Add-on regulatory classification only |
| MDCG 2019-11 (qualification and classification of software under MDR and IVDR) | Add-on regulatory classification only |
| IEC 62304 (medical device software life cycle; the add-on cites 2006+A1:2015), ISO 14971 (risk management), IEC 62366-1 (usability engineering), ISO 13485 (quality management) | Add-on regulatory documents (`docs/regolatorio/`) and the "regulatory mindset" of the website. Editions other than IEC 62304 are not stated in the sources. |
| The Glossary of Prosthodontic Terms, 9th ed. (Academy of Prosthodontics, 2017) | Terminology; see section 1.9 |

### 5.2 Protocols and formats

| Item | Title | Where it is used |
| --- | --- | --- |
| [RFC 6749](https://www.rfc-editor.org/rfc/rfc6749) | The OAuth 2.0 Authorization Framework | `dc-auth-client` (`http.rs`, `lib.rs`) |
| [RFC 7636](https://www.rfc-editor.org/rfc/rfc7636) | Proof Key for Code Exchange by OAuth Public Clients (PKCE, S256) | `dc-auth-client/src/pkce.rs` |
| [RFC 8252](https://www.rfc-editor.org/rfc/rfc8252) | OAuth 2.0 for Native Apps (loopback redirect) | `dc-auth-client/src/callback.rs`, `oidc.rs` |
| [RFC 9207](https://www.rfc-editor.org/rfc/rfc9207) | OAuth 2.0 Authorization Server Issuer Identification | `dc-auth-client/src/callback.rs` |
| [RFC 7009](https://www.rfc-editor.org/rfc/rfc7009) | OAuth 2.0 Token Revocation | `dc-auth-client/src/client.rs` |
| [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html) | Sakimura N, Bradley J, Jones M, de Medeiros B, Mortimore C | Sign-in flow, id_token checks (`dc-auth-client/src/oidc.rs`, `jwt.rs`) |
| [RFC 8032](https://www.rfc-editor.org/rfc/rfc8032) | Edwards-Curve Digital Signature Algorithm (EdDSA, Ed25519) | id_token signatures (`jwt.rs`); update manifest signing (`packaging/update-manifest.py`) |
| [minisign](https://jedisct1.github.io/minisign/) | Signature format of the update manifest | `dc-update`, `packaging/` |
| [RFC 3161](https://www.rfc-editor.org/rfc/rfc3161) | Internet X.509 PKI Time-Stamp Protocol | Authenticode time stamps (`packaging/windows/authenticode.sh`); [SSL.com repository](https://www.ssl.com/repository/) for the time-stamp root |
| [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) | Date and Time on the Internet: Timestamps | Project and scan time stamps (`dc-workspace`, `dc-scan-ui`) |
| [RFC 5545](https://www.rfc-editor.org/rfc/rfc5545) | iCalendar | Aligner change-schedule export (`dca-algo/src/schedule.rs`) |

## 6. Printing: file format and printer protocol

Sources of the print feature (print-ready files for the Elegoo Saturn 4 Ultra 16K, GOO V3 and SDCP V3). Notes: the project's print plan. Only documented facts (offsets, values, command numbers) are taken; no code of GPL or AGPL projects is copied.

| Source | Type | Licence stated | URL | Used for |
| --- | --- | --- | --- | --- |
| Elegoo, "Goo Format Spec V1.2" | File format specification | Repository GPL-3.0, holds the spec only | [github.com/elegooofficial/GOO](https://github.com/elegooofficial/GOO) | GOO V3 writer and reader |
| CBD Technology, SDCP V3.0.0 (Smart Device Control Protocol) | Protocol specification | "Open protocol", no licence file | [GitHub](https://github.com/cbd-tech/SDCP-Smart-Device-Control-Protocol-V3.0.0) | SDCP V3 client (discovery, status, upload, print control) |
| Elegoo, elegoo-link SDK | Vendor SDK | Apache-2.0 | [GitHub](https://github.com/elegooofficial/elegoo-link) | Upload and command logic (ported with attribution where used) |
| alfiedennen, SDCP V3 on the Saturn 4 Ultra 16K, firmware V1.5.6 | Community notes | MIT | [GitHub](https://github.com/alfiedennen/sdcp-saturn-4-ultra) | Quirks of the firmware |
| danielcherubini, Home Assistant Elegoo integration | Community project | MIT | [GitHub](https://github.com/danielcherubini/elegoo-homeassistant) | Status model facts |
| connorslade, `goo` crate | Community library | MIT | [GitHub](https://github.com/connorslade/goo) | Reference for the GOO layout |
| UVtools `GooFile.cs` and issues #1013, #997, #1162 | Community code and issues | AGPL-3.0 (facts only) | [GooFile.cs](https://github.com/sn4k3/UVtools/blob/master/UVtools.Core/FileFormats/GooFile.cs); [issue 1013](https://github.com/sn4k3/UVtools/issues/1013) | Field facts and printer quirks only |
| Bulrok, saturn4-bridge-linux | Community code | GPL-3.0 (facts only) | [GitHub](https://github.com/Bulrok/saturn4-bridge-linux) | SDCP behaviour facts only |
| connorslade, mslicer, printer compatibility | Community slicer | GPL-3.0 (facts only) | [GitHub](https://github.com/connorslade/mslicer); [docs](https://mslicer.com/docs/printer-compatibility) | Printer compatibility facts only |
| Elegoo, Saturn 4 Ultra 16K product page | Vendor page | n/a | [us.elegoo.com](https://us.elegoo.com/products/saturn-4-ultra-16k-10inch-monochrome-lcd-resin-3d-printer) | Printer specification |
| Elegoo, Saturn 4 Ultra 16K user manual V2 (2024-10-21) | Vendor manual | n/a | [PDF](https://www.123-3d.nl/pdf/DKI00322_Manual_EN.pdf) | Printer specification |
| Elegoo Wiki, USB drive and file names | Vendor wiki | n/a | [link](https://wiki.elegoo.com/troubleshooting/lcd-printer/usb-drive-not-inserted) | File-name rules |
| Tran TBV, Pham TNC (2026). *Effect of 3D-printed model base height on thickness distribution of thermoformed Zendura FLX dual-layer clear aligners: an in vitro study.* Front Dent Med 7:1889969 | Paper | n/a | [`10.3389/fdmed.2026.1889969`](https://doi.org/10.3389/fdmed.2026.1889969) (Crossref confirmed); [PMC13630649](https://pmc.ncbi.nlm.nih.gov/articles/PMC13630649) | Model base height (thermoforming option) |
| Formlabs, thermoformed aligners on printed models (2018) | Vendor guide | n/a | [PDF](https://media.mikran.pl/image/cache/catalog/mikran/banners//51/drukowanie-modeli-pod-retainery-retainer-model.pdf) | Model design for thermoforming |
| RayForm, Saturn 4 Ultra 16K dental resin settings (2026-10-07) | Vendor blog | n/a | [link](https://www.rayformtech.com/elegoo-saturn-4-ultra-16k-resin-settings.html) | Exposure setting ranges (to confirm with the resin maker) |
| Apple TN3179, understanding local network privacy | Vendor technical note | n/a | [link](https://developer.apple.com/documentation/technotes/tn3179-understanding-local-network-privacy) | macOS local-network permission |
| Microsoft, Windows Firewall CSP | Vendor documentation | n/a | [link](https://learn.microsoft.com/en-us/windows/client-management/mdm/firewall-csp) | Unicast replies to a broadcast on Windows |
| firewalld issue 848 | Issue | n/a | [link](https://github.com/firewalld/firewalld/issues/848) | Unicast replies to a broadcast on Linux |

Elegoo, Saturn and the other product names are trademarks of their owners. DentalCraft is not affiliated with or endorsed by them.

## 7. Cited only in the Blender add-on (not used in DentalCraft code)

The planning documents of the add-on `blender-ortho-aligner` cite the following works. They are not part of `evidence.rs` and no DentalCraft code depends on them. They are listed so that nothing the author read for the algorithms is missing. DOIs were checked in Crossref on 2026-11-21.

| Authors | Year | Title | Venue | DOI | Cited in |
| --- | --- | --- | --- | --- | --- |
| American Board of Orthodontics | 2012 | Grading System for Dental Casts and Panoramic Radiographs (revisione giugno 2012) | ABO, St. Louis; americanboardortho.com/media/1191/grading-system-casts-radiographs.pdf |  | Add-on planning notes (`docs/superpowers/plans/`) |
| Alsharif K, Ngan P, Guan G, Mamboleo E, Ouldyerou A, Merdji A, Mukdadi OM | 2026 | Effects of attachment designs on clear aligner tooth movement: A finite element analysis | PLoS One 21(3):e0327076 | [`10.1371/journal.pone.0327076`](https://doi.org/10.1371/journal.pone.0327076) | Add-on planning notes (`docs/superpowers/plans/`) |
| Fan D, Liu H, Yuan CY, Wang SY, Wang PL | 2022 | Effectiveness of the attachment position in molar intrusion with clear aligners: a finite element study | BMC Oral Health 22(1):474 | [`10.1186/s12903-022-02472-z`](https://doi.org/10.1186/s12903-022-02472-z) | Add-on planning notes (`docs/superpowers/plans/`) |
| Gomez JP, Pena FM, Martinez V, Giraldo DC, Cardona CI | 2015 | Initial force systems during bodily tooth movement with plastic aligners and composite attachments: A three-dimensional finite element analysis | Angle Orthod 85(3):454-460 | [`10.2319/050714-330.1`](https://doi.org/10.2319/050714-330.1) | Add-on planning notes (`docs/superpowers/plans/`) |
| Johnston CD, Burden DJ, Stevenson MR | 1999 | The influence of dental to facial midline discrepancies on dental attractiveness ratings | Eur J Orthod 21(5):517-522 | [`10.1093/ejo/21.5.517`](https://doi.org/10.1093/ejo/21.5.517) | Add-on planning notes (`docs/superpowers/plans/`) |
| Kaur H, Subramanian A, Mah J, Heo G, Major PW, Romanyk DL | 2025 | In Vitro Biomechanics of Attachment Use and Their Placement for Extrusive Tooth Movement by Aligner Mechanotherapy | Orthod Craniofac Res 28(3):534-539 | [`10.1111/ocr.12893`](https://doi.org/10.1111/ocr.12893) | Add-on planning notes (`docs/superpowers/plans/`) |
| Kim WH, Hong K, Lim D, Lee JH, Jung YJ, Kim B | 2020 | Optimal Position of Attachment for Removable Thermoplastic Aligner on the Lower Canine Using Finite Element Analysis | Materials 13(15):3369 | [`10.3390/ma13153369`](https://doi.org/10.3390/ma13153369) | Add-on planning notes (`docs/superpowers/plans/`) |
| Kulkarni P, Batra P, Vaiid N | 2026 | Evaluating the impact of attachment designs on canine derotation in clear aligner therapy: a finite element analysis | Prog Orthod 27(1):15 | [`10.1186/s40510-026-00619-0`](https://doi.org/10.1186/s40510-026-00619-0) | Add-on planning notes (`docs/superpowers/plans/`) |
| Lear M, Akbari A, Robertson O, Magura J, Bojrab A, Eckert G, Chen J, Conley RS, Turkkahraman H | 2025 | In Vitro Comparison of Direct Attachment Shape and Size on the Orthodontic Forces and Moments Generated by Thermoplastic Aligners During Expansion | Orthod Craniofac Res 28(2):242-252 | [`10.1111/ocr.12865`](https://doi.org/10.1111/ocr.12865) | Add-on planning notes (`docs/superpowers/plans/`) |
| Mazzeo F, Marchese E, Assumma V, Sepe J, Perillo L | 2013 | A new device (FAQ.FIX) for orthodontic bracket placement in straight wire technique | Prog Orthod 14:23 | [`10.1186/2196-1042-14-23`](https://doi.org/10.1186/2196-1042-14-23) | Add-on planning notes (`docs/superpowers/plans/`) |
| Sever C, Arslan C | 2025 | Evaluation of Compatibility of Different Attachment Types Used in Orthodontic Clear Aligners with Electron Microscopy | Dent J 13(8):379 | [`10.3390/dj13080379`](https://doi.org/10.3390/dj13080379) | Add-on planning notes (`docs/superpowers/plans/`) |
| Tan E, Eglenen MN | 2025 | The effectiveness of the attachment position in rotated premolar in clear aligner treatment: a finite element study | BMC Oral Health 25(1):1376 | [`10.1186/s12903-025-06071-6`](https://doi.org/10.1186/s12903-025-06071-6) | Add-on planning notes (`docs/superpowers/plans/`) |
| Valeri C, Aloisio A, Mummolo S, Quinzi V | 2022 | Performance of Rigid and Soft Transfer Templates Using Viscous and Fluid Resin-Based Composites in the Attachment Bonding Process of Clear Aligners | Int J Dent 2022:1637594 | [`10.1155/2022/1637594`](https://doi.org/10.1155/2022/1637594) | Add-on planning notes (`docs/superpowers/plans/`) |
| Weckmann J, Scharf S, Graf I, Schwarze J, Keilig L, Bourauel C, Braumann B | 2020 | Influence of attachment bonding protocol on precision of the attachment in aligner treatments | J Orofac Orthop 81(1):30-40 | [`10.1007/s00056-019-00204-7`](https://doi.org/10.1007/s00056-019-00204-7) | Add-on planning notes (`docs/superpowers/plans/`) |
| Yangin A, Camci H, Soybelli M | 2025 | Clear Aligner Attachments: A Comprehensive Review | Turk J Orthod 38(3):177-189 | [`10.4274/turkjorthod.2025.2025.7`](https://doi.org/10.4274/turkjorthod.2025.2025.7) | Add-on planning notes (`docs/superpowers/plans/`) |
| Demmel J, Nguyen HD | 2013 | Fast reproducible floating-point summation | 2013 IEEE 21st Symposium on Computer Arithmetic, 163-172 | [`10.1109/ARITH.2013.9`](https://doi.org/10.1109/ARITH.2013.9) | Add-on CUDA kernel `solve.cu` (reproducible sums) |

## 8. Tools, licences and process

| Item | Reference | Used for |
| --- | --- | --- |
| Kani Rust Verifier | [github.com/model-checking/kani](https://github.com/model-checking/kani) | Bounded model checking of the laws in `docs/kani.md` |
| PolyForm Noncommercial License 1.0.0 | [polyformproject.org](https://polyformproject.org/licenses/noncommercial/1.0.0) (text taken from the official [polyform-licenses repository](https://github.com/polyformproject/polyform-licenses/blob/1.0.0/PolyForm-Noncommercial-1.0.0.md), tag 1.0.0) | Licence of the source (`LICENSE.md`) |
| Developer Certificate of Origin 1.1 | [developercertificate.org](https://developercertificate.org/) | Sign-off of contributions (`CONTRIBUTING.md`) |
| Contributor Covenant 2.1 | [contributor-covenant.org](https://www.contributor-covenant.org/version/2/1/code_of_conduct.html) | `CODE_OF_CONDUCT.md` |
| OpenRouter API (optional AI classifier of the add-on) | openrouter.ai (not checked) | Add-on only; not in DentalCraft |

The Rust and Go dependencies of the code repositories, with their licences, are listed in `THIRD-PARTY-NOTICES.md` of `dentalcraft-app`. Fonts and icons are credited in `NOTICE.md` of each repository.

## 9. Link check

Every link to a paper, document, repository, specification or vendor page in sections 2 to 8 was requested on 2026-11-21 (DOI links were checked through Crossref, DataCite and PubMed instead). All answered HTTP 200, 203 or a redirect to a page, except these:

- HTTP 202: <https://eur-lex.europa.eu/eli/reg/2016/679/oj>
- HTTP 202: <https://eur-lex.europa.eu/eli/reg/2017/745/oj>
- HTTP 403: <https://support.revopoint3d.com/hc/en-us/articles/8707367541147>
- HTTP 429: <https://us.elegoo.com/products/saturn-4-ultra-16k-10inch-monochrome-lcd-resin-3d-printer>
- HTTP 429: <https://www.revopoint3d.com/products/industry-3d-scanner-mini>

A non-200 answer does not mean the page is gone: shops and EUR-Lex answer scripted requests with 202, 403 or 429. Open those links in a browser.
