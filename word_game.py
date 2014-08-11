################################################################################
__author__ = "Zachary Yocum"
__email__  = "zyocum@brandeis.edu"
################################################################################
import os
################################################################################
# This program performs a search for solutions to a word game and prints them.
# The goal of the game is to find sets of five words that share an 
# interchangeable vowel position.  E.g., one solution to the game would be the 
# set of words set(['last', 'lest', 'list', 'lost', 'lust']), since the vowels 
# 'a', 'e', 'i', 'o', and 'u' occur in the same positions between the consonant 
# clusters 'l' and 'st'.
# The algorithm implemented in this program will run in O((n^v)^|V|) time 
# complexity where n is the number of words to test against, v is the number of 
# vowels in the nth word and V is the set of vowels.
################################################################################
# Data
# Letters that are vowels
# (except for 'y' since 'y' can't make up its mind whether it's a vowel or not)
vowels = 'aeiou'
################################################################################
# Functions
################################################################################
def skeletons(word):
    """Given a word, this function returns a list of word skeleton strings such that each individual vowel character in the word is replaced with an underscore.
    E.g., skeletons('skeleton') -> ['sk_leton', 'skel_ton', 'skelet_n']"""
    # Replace the vowel at index i with an underscore in the word
    skeletonize = lambda i : word[:i] + '_' + word[i+1:]
    # Test whether the character c is a vowel
    is_vowel = lambda c : c in vowels
    return (skeletonize(i) for i, c in enumerate(word) if is_vowel(c))

def print_solutions(words):
    """This is the main function that runs the nested loops necessary to find solutions to the game and print them as they are discovered. The dictionary is keyed on word skeletons and the values are lists of words that can be constructed by filling in the underscore in the key with a vowel.
    I.e., {'b_'     : set(['ba', 'be', 'bi', 'bo']),
           ...
           'b_efy'  : set(['beefy']),
           ...
           'h_ll'   : set(['hall', 'hell', 'hill', 'hull']),
           ...
           'l_st'   : set(['last', 'lest', 'list', 'lost', 'lust']),
           ...
           'zyth_m' : set(['zythum'])}"""
    dictionary = {}
    # Iterate over all words
    for word in words:
        # Iterate over word skeletons as dictionary keys
        for key in skeletons(word):
            # Iterate over all vowels
            for vowel in vowels:
                # Test whether filling in a vowel in the skeleton forms a word
                if key.replace('_', vowel) == word:
                    # Test if the skeleton key exists yet
                    if dictionary.get(key):
                        # Append the word to the value set
                        dictionary[key].add(word)
                        # Test if a solution has been found and print it if so
                        if len(dictionary[key]) == len(vowels):
                            print ', '.join(sorted(dictionary[key]))
                    # If the key doesn't yet exist, create the key-value pair
                    else:
                        dictionary[key] = set([word])
################################################################################
if __name__ == '__main__':
    word_file_path = os.path.join(os.getcwd(), 'words.txt')
    words = open(word_file_path, 'r').read().strip().split('\n')
    print_solutions(words)
################################################################################
# Solutions
################################################################################
# blander, blender, blinder, blonder, blunder
# bad, bed, bid, bod, bud
# bag, beg, big, bog, bug
# bagged, begged, bigged, bogged, bugged
# bagging, begging, bigging, bogging, bugging
# bags, begs, bigs, bogs, bugs
# ball, bell, bill, boll, bull
# balled, belled, billed, bolled, bulled
# balling, belling, billing, bolling, bulling
# balls, bells, bills, bolls, bulls
# band, bend, bind, bond, bund
# bands, bends, binds, bonds, bunds
# bat, bet, bit, bot, but
# bats, bets, bits, bots, buts
# batty, betty, bitty, botty, butty
# clack, cleck, click, clock, cluck
# clacked, clecked, clicked, clocked, clucked
# clacking, clecking, clicking, clocking, clucking
# clacks, clecks, clicks, clocks, clucks
# call, cell, cill, coll, cull
# care, cere, cire, core, cure
# cares, ceres, cires, cores, cures
# cate, cete, cite, cote, cute
# cates, cetes, cites, cotes, cutes
# dab, deb, dib, dob, dub
# dacker, decker, dicker, docker, ducker
# dackers, deckers, dickers, dockers, duckers
# dae, dee, die, doe, due
# dan, den, din, don, dun
# dans, dens, dins, dons, duns
# fags, fegs, figs, fogs, fugs
# fan, fen, fin, fon, fun
# fand, fend, find, fond, fund
# gae, gee, gie, goe, gue
# gaes, gees, gies, goes, gues
# gally, gelly, gilly, golly, gully
# gat, get, git, got, gut
# hack, heck, hick, hock, huck
# hacks, hecks, hicks, hocks, hucks
# haed, heed, hied, hoed, hued
# hallo, hello, hillo, hollo, hullo
# halloed, helloed, hilloed, holloed, hulloed
# halloing, helloing, hilloing, holloing, hulloing
# hallos, hellos, hillos, hollos, hullos
# hap, hep, hip, hop, hup
# haps, heps, hips, hops, hups
# hat, het, hit, hot, hut
# hats, hets, hits, hots, huts
# lag, leg, lig, log, lug
# lagged, legged, ligged, logged, lugged
# lagger, legger, ligger, logger, lugger
# laggers, leggers, liggers, loggers, luggers
# lagging, legging, ligging, logging, lugging
# lags, legs, ligs, logs, lugs
# lang, leng, ling, long, lung
# lare, lere, lire, lore, lure
# last, lest, list, lost, lust
# minas, mines, minis, minos, minus
# moa, moe, moi, moo, mou
# ma, me, mi, mo, mu
# mall, mell, mill, moll, mull
# malls, mells, mills, molls, mulls
# mang, meng, ming, mong, mung
# mare, mere, mire, more, mure
# mares, meres, mires, mores, mures
# mase, mese, mise, mose, muse
# mases, meses, mises, moses, muses
# mass, mess, miss, moss, muss
# massed, messed, missed, mossed, mussed
# masses, messes, misses, mosses, musses
# massing, messing, missing, mossing, mussing
# massy, messy, missy, mossy, mussy
# mate, mete, mite, mote, mute
# mates, metes, mites, motes, mutes
# nab, neb, nib, nob, nub
# nabs, nebs, nibs, nobs, nubs
# nat, net, nit, not, nut
# pack, peck, pick, pock, puck
# packs, pecks, picks, pocks, pucks
# pall, pell, pill, poll, pull
# pans, pens, pins, pons, puns
# pant, pent, pint, pont, punt
# pants, pents, pints, ponts, punts
# pap, pep, pip, pop, pup
# papped, pepped, pipped, popped, pupped
# papping, pepping, pipping, popping, pupping
# pappy, peppy, pippy, poppy, puppy
# paps, peps, pips, pops, pups
# pat, pet, pit, pot, put
# pats, pets, pits, pots, puts
# patted, petted, pitted, potted, putted
# patter, petter, pitter, potter, putter
# patters, petters, pitters, potters, putters
# patting, petting, pitting, potting, putting
# rack, reck, rick, rock, ruck
# racked, recked, ricked, rocked, rucked
# racking, recking, ricking, rocking, rucking
# racks, recks, ricks, rocks, rucks
# rad, red, rid, rod, rud
# rads, reds, rids, rods, ruds
# ram, rem, rim, rom, rum
# rams, rems, rims, roms, rums
# rat, ret, rit, rot, rut
# rats, rets, rits, rots, ruts
# ratted, retted, ritted, rotted, rutted
# ratting, retting, ritting, rotting, rutting
# shat, shet, shit, shot, shut
# snab, sneb, snib, snob, snub
# snabs, snebs, snibs, snobs, snubs
# san, sen, sin, son, sun
# sans, sens, sins, sons, suns
# saps, seps, sips, sops, sups
# sass, sess, siss, soss, suss
# track, treck, trick, trock, truck
# tracked, trecked, tricked, trocked, trucked
# tracking, trecking, tricking, trocking, trucking
# tracks, trecks, tricks, trocks, trucks
# tag, teg, tig, tog, tug
# tags, tegs, tigs, togs, tugs
# tan, ten, tin, ton, tun
# tane, tene, tine, tone, tune
# tans, tens, tins, tons, tuns
# an, en, in, on, un
# are, ere, ire, ore, ure
# as, es, is, os, us
