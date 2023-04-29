#!/usr/bin/env bash

# echo "$PWD"
dotfiles_in_prev_dir=$(find -L .. -maxdepth 1 -type f -name ".*")
# echo $dotfiles_in_prev_dir

for dotfile in $dotfiles_in_prev_dir; do
  # echo $dotfile
  if [[ $dotfile =~ .*".dvcignore" ]] || [[ $dotfile =~ .*".gitignore" ]] || [[ $dotfile =~ .*".prev" ]] || [[ $dotfile =~ .vim-arsync ]] || [[ $dotfile =~ .*"asynctasks" ]] || [[ $dotfile =~ "null-ls-root" ]] || [[ $dotfile =~ .exrc ]]; then
    echo -n ""
  else
    # echo "$dotfile"
    ln -s "$dotfile" . 2>/dev/null
  fi
done

ln -s ../.vscode . 2>/dev/null
ln -s ../.nvim.lua . 2>/dev/null
ln -s ../setup.cfg . 2>/dev/null
ln -s ../.ruff.toml . 2>/dev/null
