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

:::{tip} Placebo



Isolasi DNA bertujuan untuk memisahkan DNA dari partikel-partikel
lainnya seperti lipid, protein, polisakarida, dan zat lainnya. Isolasi DNA
berguna untuk beberapa analisis molekuler dan rekayasa genetika seperti
genom editing, transformasi dan PCR. Isolasi DNA
dilakukan dengan metode CTAB (Cetyl Trimethyl Ammonium Bromide), metode
ini pertama kali dikenalkan oleh Doyle & amp; Doyle (1990). CTAB sendiri
merupakan senyawa kimia yang memiliki kemampuan untuk menghancurkan
dinding selulosa pada tumbuhan, hal ini memudahkan dalam proses isolasi
DNA.

Isolasi DNA memiliki tiga prinsip utama yaitu penghancuran (lisis),
ektraksi atau pemisahan DNA dari selulosa dan protein, serta pemurnian
DNA. Penghancuran (lisis) dilakukan dengan cara menggerus sampel dengan
larutan CTAB dan bahan kimia yang lain dengan tujuan agar DNA yang ada
pada sampel dapat dipisahkan dari sel-sel yang sudah terikat oleh bahan kimia
pengikat. Untuk pemurnian DNA dilakukan dengan cara mensterilkan DNA
yang telah terikat dan disimpan hingga akan dilanjutkan pada tahap PCR.

:::

:::{important} ELI5

Lorem Ipsum

:::

:::{tip} Untuk Pengajar
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
- Sampel spons
- TE Buffer ([Tris-EDTA Buffer](https://en.wikipedia.org/wiki/TE_buffer))
- CTAB ([Cetyl Trimethyl Ammonium Bromide](https://en.wikipedia.org/wiki/Cetrimonium_bromide#:~:text=DNA%20extractionedit))
- Amonium asetat 
- NaCl 5 M 
- [Fenol](https://en.wikipedia.org/wiki/Phenol) 
- [Kloroform](https://en.wikipedia.org/wiki/Chloroform) 
- iAmOH ([Isoamil alkohol](https://en.wikipedia.org/wiki/Isoamyl_alcohol)[^1])
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

:::{figure} ./pcia.svg
:label: fig:pcia

Komposisi PCIA dan CIAA
:::


[^1]: Isoamil alkohol adalah alkohol berantai cabang yang digunakan sebagai komponen dalam buffer ekstraksi organik untuk mencegah denaturasi protein. 
Agen penghilang busa (defoaming agent) menstabilkan antarmuka pemisahan fase selama ekstraksi fenol dalam prosedur pemurnian genomik molekuler dan pemulihan DNA [@IsoamylAlcohol].

[^2]: Campuran fenol:kloroform:isoamil alkohol adalah reagen khusus yang digunakan untuk pemisahan fase cair asam nukleat dari protein. 
Campuran PCI ini memfasilitasi ekstraksi organik dan denaturasi protein dalam berbagai protokol profesional pemurnian DNA genomik [@PhenolChloroformIsoamyl].

### Pembuatan CTAB

- EDTA ([EthyleneDiamineTetraAcetic acid](https://en.wikipedia.org/wiki/Ethylenediaminetetraacetic_acid))

## Prosedur

- Prosedur
- Diagram alur

Prosedur yang tercantum disini merupakan: modifikasi dari beberapa referensi; penyesuaian terhadap waktu praktikum yang tersedia dan; penyesuaian terhadap alat dan bahan yang tersedia.

::::{tab-set}

:::{tab-item} Bakteri
:sync: tab-bakteri

### Isolasi Bakteri

[need citation]

```{include} ./_generated/prosedur-bakteri.md
```
:::

:::{tab-item} Rumput Laut
:sync: tab-rumputlaut

### Isolasi Rumput Laut

[need citation]

```{include} ./_generated/prosedur-rumputlaut.md
```

:::

:::{tab-item} Hewan (Spons)
:sync: tab-hewan

### Isolasi Spons

[@hillOriginPaxSix2010]

```{include} ./_generated/prosedur-spons.md
```

:::

::::

DNA hasil isolasi disimpan pada suhu −20 °C hingga digunakan untuk proses PCR.  

