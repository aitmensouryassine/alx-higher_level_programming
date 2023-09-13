#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nbIccur = 0;
  for (const elmt of list) {
    if (elmt === searchElement) nbIccur++;
  }
  return nbIccur;
};
