# File Stream Simulator

A Python script to simulate file system streaming from a file of delimiter separated values/points/columns per line/trajectory/row.

## Usage

```bash
python3 parser.py [-h] [-d DELAY] [-min MIN_VAL] [-max MAX_VAL] [-i INPUT_FILE] [-o OUTPUT_DIR] [-c] [-s STARTFROM] [-l LIMIT] [-de DELIMITER] [-sc STREAM_COLUMNS]
```

```bash
optional arguments:
  -h, --help            show this help message and exit
  -d DELAY, --delay DELAY   Streaming Delay in seconds to generate a new values file for each trajectory (line) in output dir
  -min MIN_VAL, --min_val MIN_VAL   Minimum number of points in a line to be considered significant trajectory (line)
  -max MAX_VAL, --max_val MAX_VAL   Stream this many number of separate points file
  -i INPUT_FILE, --input_file INPUT_FILE    Path to file of line-separated trajectories of comma-sep points which should be read and parsed for streaming
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR    Output Directory to stream to (will generate a new file every streaming delay)
  -c, --cumulative      Stream Cumulatively (Append new points to previous points in new files)
  -s STARTFROM, --startFrom STARTFROM   Start from # of Trajectories upto limit defined by -l
  -l LIMIT, --limit LIMIT   Maximum number of values / trajectories to consider
  -de DELIMITER, --delimiter DELIMITER  Delimiter that separates points in each line
  -sc STREAM_COLUMNS, --stream_columns STREAM_COLUMNS   Stream Columns (Values/Points) or Rows (Lines/Trajectories)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)