import twint

# Configure
c = twint.Config()
c.Username = "cyber_ministry"
c.Search = ""

# Run
twint.run.Search(c)