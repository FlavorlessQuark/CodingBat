def string_splosion(str):
  return "".join([str[:x] for x in range(len(str) + 1)])
