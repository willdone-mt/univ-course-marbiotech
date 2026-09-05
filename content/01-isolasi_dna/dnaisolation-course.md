---
bibliography: ../../reference.bib
exports:
- id: dnaisolation-course-pdf
  format: typst
  template: https://github.com/myst-templates/plain_typst_book.git
  show_ToC: false
  papersize: a5
downloads:
- id: dnaisolation-course-pdf
  title: Unduh Halaman Ini (PDF)
- id: full-book-pdf
  title: Unduh Buku Lengkap (PDF)
---

# Isolasi DNA

- Apa itu isolasi DNA
- Prinsip
- Alur secara garis besar

:::{tip} ELI5

Lorem Ipsum

:::

:::{important} Untuk Pengajar
:class: dropdown

Silahkan pergi menuju [dokumen ini untuk cara mengajarinya](dnaisolation-teach.ipynb)
:::

## Alat dan Bahan

::::{grid} 1 1 2 2

:::{grid-item}
:columns: 1

#### Alat


- [Micro(centrifuge )tube](https://www.accumaxlab.com/microcentrifuge-tubes/) 
  - 1,5 mL 
  - 2 mL 
- [Centrifuge](https://en.wikipedia.org/wiki/Centrifuge) 
- Spindown 
- Waterbath 
- Vortex 
- Heatblock/heatlock 
- Freezer
- Neraca Ohaus 
- Mikropipet 
- Tip mikropipet 
- Mortar dan pestle 
- Ose 
- Silet 

:::

:::{grid-item}
:columns: 1

#### Bahan

- Media kultur bakteri 
- Sampel bakteri 
- Sampel rumput laut 
- Sampel filet ikan 
- TE Buffer ([Tris-EDTA Buffer](https://en.wikipedia.org/wiki/TE_buffer))
- CTAB ([Cetyl Trimethyl Ammonium Bromide](https://en.wikipedia.org/wiki/Cetrimonium_bromide#:~:text=DNA%20extractionedit))
- Amonium asetat 
- NaCl 5 M 
- Fenol 
- Kloroform 
- [Isoamil alkohol](https://en.wikipedia.org/wiki/Isoamyl_alcohol)[^1]
- CIAA (Kloroform:Isoamil Alkohol = 24:1)
- PCIA[^2] (Fenol:kloroform:isoamil alkohol = 25:24:1) 
- Etanol absolut dingin 
- Etanol 70% dingin 
- PVP ([PolyVinylPyrrolidone](https://en.wikipedia.org/wiki/Polyvinylpyrrolidone))
- β-mercaptoethanol 
- Longmire Buffer 
- Proteinase K 
- Isopropanol dingin 
- Nitrogen cair 

:::

::::

~~~mermaid
flowchart TD

C[Kloroform]

IA[Isoamil Alkohol]

F[Fenol]

CIAA

FCIAA[Fenol:Kloroform:Isoamil Alkohol]

C --> CIAA
IA --> CIAA

CIAA --> FCIAA
F --> FCIAA
~~~

### Pembuatan CTAB

- EDTA ([EthyleneDiamineTetraAcetic acid](https://en.wikipedia.org/wiki/Ethylenediaminetetraacetic_acid))

## Prosedur

- Prosedur
- Diagram alur



[^1]: Isoamil alkohol adalah alkohol berantai cabang yang digunakan sebagai komponen dalam buffer ekstraksi organik untuk mencegah denaturasi protein. 
Agen penghilang busa (defoaming agent) menstabilkan antarmuka pemisahan fase selama ekstraksi fenol dalam prosedur pemurnian genomik molekuler dan pemulihan DNA [@IsoamylAlcohol].

[^2]: Campuran fenol:kloroform:isoamil alkohol adalah reagen khusus yang digunakan untuk pemisahan fase cair asam nukleat dari protein. 
Campuran PCI ini memfasilitasi ekstraksi organik dan denaturasi protein dalam berbagai protokol profesional pemurnian DNA genomik [@PhenolChloroformIsoamyl].