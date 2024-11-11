<h1>About</h1>
<h4>Convect your csv files in xlsx files</h4>
<h1>Install</h1>

### For install, use:
    pip install -r requirements.txt

# Run

    python conv.py G:\files G:\files\xlsx
### With remove:

    python conv.py G:\files G:\files\xlsx --rm=true

<h1>Arguments</h1>

#### The first arg is csv files folder, example:

    python conv.py G:\files
#### Second arg is xlsx files folder, example:

    python conv.py G:\files G:\files\xlsx
#### You can also use the same folder as for csv files, example:

    python conv.py G:\files 
#### Last arg is responsible for deleting files, example:

    python conv.py G:\files G:\files\xlsx --rm=true
#### If don't need to delete it, then just don't write argument, example:

    python conv.py G:\files G:\files\xlsx
### Good luck
