# Large-scale File Fragment Type Identification using Neural Networks

FiFTy is a file type classifier that works much like the ``file`` command in Unix-like systems but with much more cool techniques up its sleeve. It beats several previous benchmarks on the biggest play field there is right now.  FiFTy comes with pre-trained models for six scenarios and for block sizes of 512 and 4096 bytes.  It is retrainable for a subset of our studied filetypes and can be scaled up for newer filetypes and other block sizes too. Please find our corresponding paper at https://arxiv.org/abs/1908.06148 and the ready-to-use open access datasets at [FFT-75](https://ieee-dataport.org/open-access/file-fragment-type-fft-75-dataset).

## List of Filetypes
The classifier has been tested on the following 75 filetypes :--

| | | | | | 
| :---: | :---: | :---: | :---: | :---: |
| ARW | CR2 | DNG | GPR | NEF |
| NRW | ORF | PEF | RAF | RW2 |
| 3FR | JPG | TIFF | HEIC | BMP |
| GIF | PNG | AI | EPS | PSD |
| MOV | MP4 | 3GP | AVI | MKV |
| OGV | WEBM | APK | JAR | MSI |
| DMG | 7Z | BZ2 | DEB | GZ |
| PKG | RAR | RPM | XZ | ZIP |
| EXE | MACH-O | ELF | DLL | DOC |
| DOCX | KEY | PPT | PPTX | XLS |
| XLSX | DJVU | EPUB | MOBI | PDF |
| MD | RTF | TXT | TEX | JSON |
| HTML | XML | LOG | CSV | AIFF |
| FLAC | M4A | MP3 | OGG | WAV |
| WMA | PCAP | TTF | DWG | SQLITE |


## Scenario Description
We present [models](https://github.com/mittalgovind/fifty/tree/master/fifty/utilities/models) for _six_ scenarios on two popular block sizes of __512__ and __4096__ bytes. File type selection reflects focus on media carving applications, where scenarios \#3 to \#6 are the most relevant:

1. **\#1 (All; 75 classes)**: All filetypes are separate classes; this is the most generic case and can be aggregated into more specialized use-cases.

2. **\#2 (Use-specific; 11)**: Filetypes are grouped into 11 classes according to their use; this information may be useful for more-detailed, hierarchical classification or for determining the primary use of an unknown device.

3. **\#3 (Media Carver - Photos \& Videos; 25)**: Every filetype tagged as a bitmap (6), RAW photo (11) or video (7) is considered as a separate class;  all remaining types are grouped into one _other_ class. 

4. **\#4 (Coarse Photo Carver; 5)**: Separate classes for different photographic types: JPEG, 11 raw images, 7 videos, 5 remaining bitmaps are grouped into one separate class per category; all remaining types are grouped into one _other_ class.  

5. **\#5 (Specialized JPEG Carver; 2)**: JPEG is a separate class and the remaining 74 filetypes are grouped into one _other_ class; scenario intended for analyzing disk images from generic devices.

1. **\#6 (Camera-Specialized JPEG Carver; 2)**: JPEG is a separate class and the remaining photographic/video types (11 raw images, 3GP, MOV, MKV, TIFF and HEIC) are grouped into one _other_ class; scenario intended for analyzing SD cards from digital cameras.
