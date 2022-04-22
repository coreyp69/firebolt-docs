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
// replace with namespace name
const namespaceId = new symbol_sdk_1.NamespaceId('foo');
// replace with address
const rawAddress = 'TCHBDE-NCLKEB-ILBPWP-3JPB2X-NY64OE-7PYHHE-32I';
const address = symbol_sdk_1.Address.createFromRawAddress(rawAddress);
/* end block 01 */
/* start block 02 */
// replace with network type
const networkType = symbol_sdk_1.NetworkType.TEST_NET;
const addressAliasTransaction = symbol_sdk_1.AliasTransaction.createForAddress(
  symbol_sdk_1.Deadline.create(epochAdjustment),
  symbol_sdk_1.AliasAction.Link,
  namespaceId,
  address,
  networkType,
  symbol_sdk_1.UInt64.fromUint(2000000),
);
// replace with private key
const privateKey =
  '1111111111111111111111111111111111111111111111111111111111111111';
const account = symbol_sdk_1.Account.createFromPrivateKey(
  privateKey,
  networkType,
);
// replace with meta.networkGenerationHash (nodeUrl + '/node/info')
const networkGenerationHash =
  '1DFB2FAA9E7F054168B0C5FCB84F4DEB62CC2B4D317D861F3168D161F54EA78B';
const signedTransaction = account.sign(
  addressAliasTransaction,
  networkGenerationHash,
);
// replace with node endpoint
const nodeUrl = 'NODE_URL';
const repositoryFactory = new symbol_sdk_1.RepositoryFactoryHttp(nodeUrl);
const transactionHttp = repositoryFactory.createTransactionRepository();
transactionHttp.announce(signedTransaction).subscribe(
  (x) => console.log(x),
  (err) => console.error(err),
);
/* end block 02 */
