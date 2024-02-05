-- Copyright (c) MonetLoader, 2023
-- Built-in library: jsoncfg
-- Lua package is distributed under the MIT license

local PATH_SEPARATOR = '/'
if MONET_VERSION == nil then
  PATH_SEPARATOR = '\\'
end

local function deepcopy(o, seen)
  seen = seen or {}
  if o == nil then return nil end
  if seen[o] then return seen[o] end

  local no
  if type(o) == 'table' then
    no = {}
    seen[o] = no

    for k, v in next, o, nil do
      no[deepcopy(k, seen)] = deepcopy(v, seen)
    end
    setmetatable(no, deepcopy(getmetatable(o), seen))
  else -- number, string, boolean, etc
    no = o
  end
  return no
end

local function deepmerge(a, b)
  for k, v in next, b, nil do
    if a[k] == nil then
      a[deepcopy(k)] = deepcopy(v)
    else
      if type(v) == 'table' and type(a[k]) == 'table' then
        deepmerge(a[k], v)
      end
    end
  end
end

local function load(default, filename, extension)
  local default = default or {}
  local filename = filename or script.this.filename
  local extension = extension or '.json'

  filename:gsub('\\', PATH_SEPARATOR)
  if MONET_VERSION ~= nil then
    filename:gsub('moonloader/', 'monetloader/')
  end

  local filepath1 = getWorkingDirectory() .. PATH_SEPARATOR .. 'config' .. PATH_SEPARATOR .. filename .. extension
  local filepath2 = getWorkingDirectory() .. PATH_SEPARATOR .. 'config' .. PATH_SEPARATOR .. filename
  local filepath3 = filename

  local file = io.open(filepath1, 'r')
  if not file then
    file = io.open(filepath2, 'r')
  end
  if not file then
    file = io.open(filepath3, 'r')
  end

	if file then
		local loaded = decodeJson(file:read('*a'))
    file:close()
    if loaded == nil then
      return deepcopy(default)
    end

    deepmerge(loaded, default)
    return loaded
	else
    return deepcopy(default)
  end
end

local function save(data, filename, extension)
  local filename = filename or script.this.filename
  local extension = extension or '.json'

  filename:gsub('\\', PATH_SEPARATOR)
  if MONET_VERSION ~= nil then
    filename:gsub('moonloader/', 'monetloader/')
  end

  local filepath = getWorkingDirectory() .. PATH_SEPARATOR .. 'config' .. PATH_SEPARATOR
  if filename:find(PATH_SEPARATOR, 1, true) ~= nil then
    local dir = filename:match('.*' .. PATH_SEPARATOR)
    createDirectory(dir)
    filepath = filename
  elseif filename:match('%' .. extension .. '$') ~= nil then
    createDirectory(filepath)
    filepath = filepath .. filename
  else
    createDirectory(filepath)
    filepath = filepath .. filename .. extension
  end

  local file, errstr = io.open(filepath, 'w')
	if file then
		file:write(encodeJson(data))
    file:close()
    return true
	else
    print('jsoncfg: failed to open file, error:', errstr)
    return false
  end
end

return {
  load = load,
  save = save
}