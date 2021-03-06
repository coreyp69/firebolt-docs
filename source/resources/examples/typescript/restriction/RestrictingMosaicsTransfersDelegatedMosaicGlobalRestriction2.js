'use strict';
/*
 *
 * Copyright 2018-present NEM
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */
Object.defineProperty(exports, '__esModule', { value: true });
const symbol_sdk_1 = require('symbol-sdk');
// Retrieve from node's /network/properties or RepositoryFactory
const epochAdjustment = 123456789;
/* start block 01 */
// replace with cc.shares mosaic id
const sharesIdHex = '7cdf3b117a3c40cc';
const sharesId = new symbol_sdk_1.MosaicId(sharesIdHex);
// replace with kyc mosaic id
const kycIdHex = '183D0802BCDB97AF';
const kycId = new symbol_sdk_1.MosaicId(kycIdHex);
// replace with network type
const networkType = symbol_sdk_1.NetworkType.TEST_NET;
const key = symbol_sdk_1.KeyGenerator.generateUInt64Key(
  'IsVerified'.toLowerCase(),
);
const transaction = symbol_sdk_1.MosaicGlobalRestrictionTransaction.create(
  symbol_sdk_1.Deadline.create(epochAdjustment),
  sharesId, // mosaicId
  key, // restictionKey
  symbol_sdk_1.UInt64.fromUint(0), // previousRestrictionValue
  symbol_sdk_1.MosaicRestrictionType.NONE, // previousRestrictionType
  symbol_sdk_1.UInt64.fromUint(2), // newRestrictionValue
  symbol_sdk_1.MosaicRestrictionType.EQ, // newRestrictionType
  networkType,
  kycId, // referenceMosaicId
  symbol_sdk_1.UInt64.fromUint(2000000),
);
const comfyClothingCompanyPrivateKey =
  'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF';
const comfyClothingCompanyAccount = symbol_sdk_1.Account.createFromPrivateKey(
  comfyClothingCompanyPrivateKey,
  networkType,
);
// replace with meta.networkGenerationHash (nodeUrl + '/node/info')
const networkGenerationHash =
  '1DFB2FAA9E7F054168B0C5FCB84F4DEB62CC2B4D317D861F3168D161F54EA78B';
const signedTransaction = comfyClothingCompanyAccount.sign(
  transaction,
  networkGenerationHash,
);
console.log(signedTransaction.hash);
// replace with node endpoint
const nodeUrl = 'NODE_URL';
const repositoryFactory = new symbol_sdk_1.RepositoryFactoryHttp(nodeUrl);
const transactionHttp = repositoryFactory.createTransactionRepository();
transactionHttp.announce(signedTransaction).subscribe(
  (x) => console.log(x),
  (err) => console.error(err),
);
/* end block 01 */
