#!/usr/bin/env python3
"""
  Purpose:  This script uses pulumi to deploy the required resources 
    to stand up a Kong Gateway on AKS with KIC.
  Requirements:  Python3 with the import modules available and IAM access.
  Author:  Chad Ingle
"""
import pulumi, os, sys, json, base64
import pulumi_azure_native as azure_native
import pulumi_tls as tls

# Create our Resource Group to store everything for easy cleanup
resource_group = azure_native.resources.ResourceGroup(
    "kong-aks-cluster-rg",
    resource_group_name = "kong-aks-cluster-rg",
    location = "westus2"
)

# Create VNET and Public and Private Subnets
virtual_network = azure_native.network.VirtualNetwork(
    "kong-aks-cluster-vnet",
    address_space = azure_native.network.AddressSpaceArgs(
        address_prefixes=["10.0.0.0/16"],
    ),
    location = "westus2",
    resource_group_name = resource_group.name,
    virtual_network_name = "kong-aks-cluster-vnet"
)

public_subnet = 
