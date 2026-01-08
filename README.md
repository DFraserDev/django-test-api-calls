# Django Test API Calls

This project was designed as a means to be self-taught in how to create an API through a Django server.

## Hierarchy
<b>Project Directory</b> - `testapi` directory<br />
<b>App Directory</b> - `mainapitester` directory

## Making the API Calls
The project has two API calls you can make:

• `http://<ip_address>:<port>/api/testcall`<br />
• `http://<ip_address>:<port>/api/ff6/bestiary/<enemy_number>`

The first is just a simple Response with some text.

The second API call is dynamic and uses an old script I created that contains data from Final Fantasy 6's Bestiary on the Game Boy Advance.
This URL takes in a number from 1-384, and will return an error message when `<enemy_number>` is out of range.



<details>
  <summary>List of Enemies (NOTE: This is a long expandable list)</summary>
  
  <ul>
<li>1 - Guard</li>
<li>2 - Silver Lobo</li>
<li>3 - Megalodoth</li>
<li>4 - Wererat</li>
<li>5 - Spritzer</li>
<li>6 - Bandit</li>
<li>7 - Leaf Bunny</li>
<li>8 - Darkwind</li>
<li>9 - Sand Ray</li>
<li>10 - Alacran</li>
<li>11 - Foper</li>
<li>12 - Hornet</li>
<li>13 - Urok</li>
<li>14 - Belmodar</li>
<li>15 - Unseelie</li>
<li>16 - Mu</li>
<li>17 - Zaghrem</li>
<li>18 - Trillium</li>
<li>19 - Gorgias</li>
<li>20 - Cirpius</li>
<li>21 - Lesser Lopros</li>
<li>22 - Nautiloid</li>
<li>23 - Exocite</li>
<li>24 - Heavy Armor</li>
<li>25 - Commander</li>
<li>26 - Vector Hound</li>
<li>27 - Cartagra</li>
<li>28 - Acrophies</li>
<li>29 - Gold Bear</li>
<li>30 - Valeor</li>
<li>31 - Wild Rat</li>
<li>32 - Stray Cat</li>
<li>33 - Aepyornis</li>
<li>34 - Nettlehopper</li>
<li>35 - Chippirabbit</li>
<li>36 - Captain</li>
<li>37 - Imperial Soldier</li>
<li>38 - Templar</li>
<li>39 - Satellite</li>
<li>40 - Ghost</li>
<li>41 - Poplium</li>
<li>42 - Cloud</li>
<li>43 - Angel Whisper</li>
<li>44 - Oversoul</li>
<li>45 - Bomb</li>
<li>46 - Living Dead</li>
<li>47 - Apparition</li>
<li>48 - Siegfried</li>
<li>49 - Opinicus Fish</li>
<li>50 - Anguiform</li>
<li>51 - Aspiran</li>
<li>52 - Actinian</li>
<li>53 - Fidor</li>
<li>54 - Corporal</li>
<li>55 - Hunting Hound</li>
<li>56 - Fossil Dragon</li>
<li>57 - Vulture</li>
<li>58 - Iron Fist</li>
<li>59 - Bloodfang</li>
<li>60 - Rock Wasp</li>
<li>61 - Paraladia</li>
<li>62 - Harvester</li>
<li>63 - Hill Gigas</li>
<li>64 - Gobbledygook</li>
<li>65 - Veil Dancer</li>
<li>66 - Stunner</li>
<li>67 - Goetia</li>
<li>68 - Litwor Chicken</li>
<li>69 - Joker</li>
<li>70 - Don</li>
<li>71 - Wyvern</li>
<li>72 - Grasswyrm</li>
<li>73 - Grenade</li>
<li>74 - Bug</li>
<li>75 - Onion Knight</li>
<li>76 - Sergeant</li>
<li>77 - Belzecue</li>
<li>78 - Proto Armor</li>
<li>79 - Trapper</li>
<li>80 - Flan</li>
<li>81 - General</li>
<li>82 - Destroyer</li>
<li>83 - Lenergia</li>
<li>84 - Magna Roader</li>
<li>85 - Magna Roader</li>
<li>86 - Chaser</li>
<li>87 - Outcast</li>
<li>88 - Provoker</li>
<li>89 - Zombie Dragon</li>
<li>90 - Antares</li>
<li>91 - Lich</li>
<li>92 - Imperial Elite</li>
<li>93 - Mega Armor</li>
<li>94 - Briareus</li>
<li>95 - Devourer</li>
<li>96 - Chimera</li>
<li>97 - Intangir</li>
<li>98 - Balloon</li>
<li>99 - Bonnacon</li>
<li>100 - Land Grillon</li>
<li>101 - Adamankary</li>
<li>102 - Mandrake</li>
<li>103 - Venobennu</li>
<li>104 - Sky Armor</li>
<li>105 - Spitfire</li>
<li>106 - Brainpan</li>
<li>107 - Misfit</li>
<li>108 - Apocrypha</li>
<li>109 - Dragon</li>
<li>110 - Platinum Dragon</li>
<li>111 - Behemoth</li>
<li>112 - Ninja</li>
<li>113 - Naude</li>
<li>114 - Fafnir</li>
<li>115 - Killer Mantis</li>
<li>116 - Peeper</li>
<li>117 - Murussu</li>
<li>118 - Gigantoad</li>
<li>119 - Land Ray</li>
<li>120 - Luna Wolf</li>
<li>121 - Black Dragon</li>
<li>122 - Rukh</li>
<li>123 - Zokka</li>
<li>124 - Nightwalker</li>
<li>125 - Scorpion</li>
<li>126 - Delta Beetle</li>
<li>127 - Vampire Thorn</li>
<li>128 - Lizard</li>
<li>129 - Devoahan</li>
<li>130 - Sandhorse</li>
<li>131 - Cancer</li>
<li>132 - Oceanus</li>
<li>133 - Desert Hare</li>
<li>134 - Humpty</li>
<li>135 - Cruller</li>
<li>136 - Dropper</li>
<li>137 - Neck Hunter</li>
<li>138 - Dante</li>
<li>139 - Bogy</li>
<li>140 - Marchosias</li>
<li>141 - Deepeye</li>
<li>142 - Mousse</li>
<li>143 - Borghese</li>
<li>144 - Malboro</li>
<li>145 - Cloudwraith</li>
<li>146 - Exoray</li>
<li>147 - Skeletal Horror</li>
<li>148 - Mugbear</li>
<li>149 - Devil Fist</li>
<li>150 - Luridan</li>
<li>151 - Punisher</li>
<li>152 - Glasya Labolas</li>
<li>153 - Gorgimera</li>
<li>154 - Twinscythe</li>
<li>155 - Death Warden</li>
<li>156 - Misty</li>
<li>157 - Rafflesia</li>
<li>158 - Still Life</li>
<li>159 - Coeurl Cat</li>
<li>160 - Crusher</li>
<li>161 - Blade Dancer</li>
<li>162 - Caladrius</li>
<li>163 - Ouroboros</li>
<li>164 - Face</li>
<li>165 - Zeveak</li>
<li>166 - Seaflower</li>
<li>167 - Galypdes</li>
<li>168 - Necromancer</li>
<li>169 - Clymenus</li>
<li>170 - Chaos Dragon</li>
<li>171 - Brachiosaur</li>
<li>172 - Tyrannosaur</li>
<li>173 - Tumbleweed</li>
<li>174 - Leap Frog</li>
<li>175 - Slagworm</li>
<li>176 - Cactuar</li>
<li>177 - Crawler</li>
<li>178 - Sprinter</li>
<li>179 - Basilisk</li>
<li>180 - Lycaon</li>
<li>181 - Greater Mantis</li>
<li>182 - Test Rider</li>
<li>183 - Wizard</li>
<li>184 - Lukhavi</li>
<li>185 - Magna Roader</li>
<li>186 - Magna Roader</li>
<li>187 - Psychos</li>
<li>188 - Garm</li>
<li>189 - Tonberry</li>
<li>190 - Onion Dasher</li>
<li>191 - Anemone</li>
<li>192 - Illuyankas</li>
<li>193 - Knotty</li>
<li>194 - Tzakmaqiel</li>
<li>195 - Zone Eater</li>
<li>196 - Vasegiatta</li>
<li>197 - Gloomwind</li>
<li>198 - Purusa</li>
<li>199 - Covert</li>
<li>200 - Kamui</li>
<li>201 - Wartpuck</li>
<li>202 - Shambling Corpse</li>
<li>203 - Amduscias</li>
<li>204 - Baalzephon</li>
<li>205 - Samurai</li>
<li>206 - Al Jabr</li>
<li>207 - Suriander</li>
<li>208 - Weredragon</li>
<li>209 - Schmidt</li>
<li>210 - Pluto Armor</li>
<li>211 - Alluring Rider</li>
<li>212 - Pandora</li>
<li>213 - Parasite</li>
<li>214 - Coco</li>
<li>215 - Io</li>
<li>216 - Armored Weapon</li>
<li>217 - Lunatys</li>
<li>218 - Figaro Lizard</li>
<li>219 - Devil</li>
<li>220 - Enuo</li>
<li>221 - Magic Urn</li>
<li>222 - Level 10 Magic</li>
<li>223 - Level 20 Magic</li>
<li>224 - Level 30 Magic</li>
<li>225 - Level 40 Magic</li>
<li>226 - Level 50 Magic</li>
<li>227 - Level 60 Magic</li>
<li>228 - Level 70 Magic</li>
<li>229 - Level 80 Magic</li>
<li>230 - Level 90 Magic</li>
<li>231 - Warlock</li>
<li>232 - Mahadeva</li>
<li>233 - Sorath</li>
<li>234 - Medusa Chicken</li>
<li>235 - Creature</li>
<li>236 - Moonform</li>
<li>237 - Aspidochelon</li>
<li>238 - Siegfried</li>
<li>239 - Yojimbo</li>
<li>240 - Dark Force</li>
<li>241 - Muud Suud</li>
<li>242 - Fiend Dragon</li>
<li>243 - Mover</li>
<li>244 - Cherry</li>
<li>245 - Vector Lythos</li>
<li>246 - Primeval Dragon</li>
<li>247 - Landworm</li>
<li>248 - Gamma</li>
<li>249 - Great Malboro</li>
<li>250 - Outsider</li>
<li>251 - Demon Knight</li>
<li>252 - Duel Armor</li>
<li>253 - Great Behemoth</li>
<li>254 - Vector Chimera</li>
<li>255 - Fortis</li>
<li>256 - Junk</li>
<li>257 - InnoSent</li>
<li>258 - Daedalus</li>
<li>259 - Ahriman</li>
<li>260 - Death Machine</li>
<li>261 - Metal Hitman</li>
<li>262 - Prometheus</li>
<li>263 - Zurvan</li>
<li>264 - Vilia</li>
<li>265 - Great Dragon</li>
<li>266 - Abaddon</li>
<li>267 - Dragon Aevis</li>
<li>268 - Dinozombie</li>
<li>269 - Death Rider</li>
<li>270 - Shield Dragon</li>
<li>271 - Maximera</li>
<li>272 - Hexadragon</li>
<li>273 - Magic Dragon</li>
<li>274 - Armodullahan</li>
<li>275 - Crystal Dragon</li>
<li>276 - Ymir</li>
<li>277 - Ymir</li>
<li>278 - Guard Leader</li>
<li>279 - Magitek Armor</li>
<li>280 - Vargas</li>
<li>281 - Ipooh</li>
<li>282 - Ultros</li>
<li>283 - Tunnel Armor</li>
<li>284 - Phantom Train</li>
<li>285 - Rhizopas</li>
<li>286 - Hell's Rider</li>
<li>287 - Kefka</li>
<li>288 - Dadaluma</li>
<li>289 - Ultros</li>
<li>290 - Ifrit</li>
<li>291 - Shiva</li>
<li>292 - Number 024</li>
<li>293 - Number 128</li>
<li>294 - Right Blade</li>
<li>295 - Left Blade</li>
<li>296 - Crane</li>
<li>297 - Crane</li>
<li>298 - Flame Eater</li>
<li>299 - Ultros</li>
<li>300 - Typhon</li>
<li>301 - Ultros</li>
<li>302 - Air Force</li>
<li>303 - Laser Gun</li>
<li>304 - Missile Bay</li>
<li>305 - Bit</li>
<li>306 - Gigantos</li>
<li>307 - Ultima Weapon</li>
<li>308 - Nelapa</li>
<li>309 - Humbaba</li>
<li>310 - Tentacle</li>
<li>311 - Tentacle</li>
<li>312 - Tentacle</li>
<li>313 - Tentacle</li>
<li>314 - Angler Whelk</li>
<li>315 - Angler Whelk</li>
<li>316 - Dullahan</li>
<li>317 - Behemoth King</li>
<li>318 - Behemoth King</li>
<li>319 - Chadarnook</li>
<li>320 - Valigarmanda</li>
<li>321 - Tonberries</li>
<li>322 - Yeti</li>
<li>323 - Curlax</li>
<li>324 - Laragorn</li>
<li>325 - Moebius</li>
<li>326 - Wrexsoul</li>
<li>327 - Soul Saver</li>
<li>328 - Master Tonberry</li>
<li>329 - Samurai Soul</li>
<li>330 - Magic Master</li>
<li>331 - Deathgaze</li>
<li>332 - Hidon</li>
<li>333 - Erebus</li>
<li>334 - Erebus</li>
<li>335 - Erebus</li>
<li>336 - Erebus</li>
<li>337 - Red Dragon</li>
<li>338 - Blue Dragon</li>
<li>339 - Gold Dragon</li>
<li>340 - Ice Dragon</li>
<li>341 - Storm Dragon</li>
<li>342 - Earth Dragon</li>
<li>343 - Skull Dragon</li>
<li>344 - Holy Dragon</li>
<li>345 - Gigantaur</li>
<li>346 - Leviathan</li>
<li>347 - Gilgamesh</li>
<li>348 - Inferno</li>
<li>349 - Rahu</li>
<li>350 - Ketu</li>
<li>351 - Ultima Buster</li>
<li>352 - Guardian</li>
<li>353 - Fiend</li>
<li>354 - Goddess</li>
<li>355 - Demon</li>
<li>356 - Short Arm</li>
<li>357 - Long Arm</li>
<li>358 - Visage</li>
<li>359 - Tiger</li>
<li>360 - Machine</li>
<li>361 - Magic</li>
<li>362 - Power</li>
<li>363 - Lady</li>
<li>364 - Rest</li>
<li>365 - Kefka</li>
<li>366 - Plague</li>
<li>367 - Flan Princess</li>
<li>368 - Neslug</li>
<li>369 - Neslug</li>
<li>370 - Earth Eater</li>
<li>371 - Gargantua</li>
<li>372 - Malboro Menace</li>
<li>373 - Abyss Worm</li>
<li>374 - Dark Behemoth</li>
<li>375 - Red Dragon</li>
<li>376 - Blue Dragon</li>
<li>377 - Gold Dragon</li>
<li>378 - Ice Dragon</li>
<li>379 - Storm Dragon</li>
<li>380 - Earth Dragon</li>
<li>381 - Skull Dragon</li>
<li>382 - Holy Dragon</li>
<li>383 - Kaiser Dragon</li>
<li>384 - Omega Weapon</li>
</ul>
</details>

## Project Setup

### Project Level Directory

The ALLOWED_HOSTS list under `settings.py` takes in list elements from a file I made called `env.py`.

In `env.py`, the list is named <b>allowed_ips</b>, which contained both a localhost address, and the address for the computer I was running on.

You will need to use ipconfig to find your computer's IP on the network and insert that as a list element.<br />
This is required for making the API call because it doesn't work with the 127.0.0.1 localhost address.
