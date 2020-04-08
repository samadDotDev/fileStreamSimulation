# File Stream Simulator

A Python script to simulate file system streaming from a file of delimiter separated values/points/columns per line/trajectory/row.

## Usage

### Quick Start

```bash
python parser.py
```

This will stream with default options selected (an existing file present in input directory will be timely streamed to multiple files in output dir).

Pass -h argument to show possible optional arguments to use this script for your own problem.

### Full Usage

```bash
python parser.py [-h] [-d DELAY] [-min MIN_VAL] [-max MAX_VAL] [-i INPUT_FILE]
                 [-o OUTPUT_DIR] [-c] [-s START_FROM] [-l LIMIT]
                 [-de DELIMITER] [-sc]
```

```bash
optional arguments:
  -h, --help            show this help message and exit
  -d DELAY, --delay DELAY
                        Streaming Delay in seconds to generate a new values
                        file for each trajectory (line) in output dir
                        (default: 1)
  -min MIN_VAL, --min_val MIN_VAL
                        Minimum number of points in a line to be considered
                        significant trajectory (line) (default: 50)
  -max MAX_VAL, --max_val MAX_VAL
                        Stream this many number of separate points file
                        (default: 50)
  -i INPUT_FILE, --input_file INPUT_FILE
                        Path to file of line-separated trajectories of comma-
                        sep points which should be read and parsed for
                        streaming (default: input/trajectory.txt)
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
                        Output Directory to stream to (will generate a new
                        file every streaming delay) (default: output/)
  -c, --cumulative      Stream Cumulatively (Append new points to previous
                        points in new files) (default: True)
  -s START_FROM, --start_from START_FROM
                        Start from Row/Line/Trajectory Number upto limit
                        defined by -l (default: 0)
  -l LIMIT, --limit LIMIT
                        Maximum number of values / trajectories to consider
                        (default: 100000)
  -de DELIMITER, --delimiter DELIMITER
                        Delimiter that separates points in each line (default:
                        ;)
  -sc, --stream_columns
                        Stream Columns (Values/Points) or Rows
                        (Lines/Trajectories) (default: True)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)