# YMM_auto_generation

This is a repository for generating slow commentary project files (ymmp) from word files.

You can specify sound effects, automatic weighting of facial expressions, background music, and fade timing.

# Environment

Windows 10 / 11

# Requirement

- [YMM4](https://manjubox.net/ymm4/ "YMM4")
- [Python above 3.11](https://www.python.org/ "python")

# Installation

```batch
mkdir $USERPROFILE$\works\[YourProjectName]  && cd $USERPROFILE$\works\[YourProjectName]
git clone https://github.com/itkmaingit/YukkuriMovieMaker4.git
cd YMM_auto_generation
.\Scripts\activate
pip install -r requirements.txt
```

# Usage

1. Please make [docx](https://github.com/itkmaingit/YukkuriMovieMaker4/blob/master/samples/0212.doc"sample.docx") and [htm](https://github.com/itkmaingit/YukkuriMovieMaker4/blob/master/samples/0212.htm "sample.htm") files like sample and place them under [YourProjectName]\\[YourMovieName].

2. (only if the first)
   Install the dictionary file within YMM4.

3. Run

```batch
cd $USERPROFILE$\works\[YourProjectName]\YMM_auto_generation
.\Scripts\activate
py unite.py
>フォルダ名を入力してください。
[YourMovieName]
```

4.  When the output is complete, enter the shortcut Ctrl+D within YMM4 to open the script, load the daihon.txt file created within [YourMovieName], and save the project file under Save the project file under \$USERPROFILE\$\works\\[YourProjectName\]\PF.

5.  Run

```batch
py main.py
>フォルダ名を入力してください。
[YourMovieName]
```

6. Open the file [YourMovieName].ymmp under PF in YMM4 and output the movie.
