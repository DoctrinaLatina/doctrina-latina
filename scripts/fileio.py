def read_csv(file_path, la, en):
  f = open(file_path, 'r')
  line = f.readline()

  line_count = 1

  while line:
    # key ^ latin line ^ english line
    # -- OR --
    # latin line ^ english line
    s = line.split('^')
    if (2 == len(s)):
      key = str(line_count)
      line_la = s[0].strip()
      line_en = s[1].strip()
    elif (3 == len(s)):
      key = s[0].strip()
      line_la = s[1].strip()
      line_en = s[2].strip()

    la[key] = line_la
    en[key] = line_en
    line = f.readline()
    line_count = line_count + 1
