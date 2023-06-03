# Really a Text File?

The magic bytes of the file are corrupted. The file is actually a JPEG with the first few bytes set as `00`. When the file is opened with notepad or any other text editor, you can see the word `JFIF` in it. THis is the ASCII representation of the magic bytes of a jpg file. Correct the magic bytes and view it in an image viewer.
