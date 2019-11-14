SELECT Opportunity__r.stonecode__c,
       OwnerId,
       Chip_Multi__c,
       Id,
       Opportunity__r.Account.Id,
       Opportunity__r.Account.Grupo_3_SF__c,
       Opportunity__r.Account.Grupo_4_SF__c,
       Opportunity__r.CreatedDate
FROM PricingObject__c
WHERE Chip_Multi__c > 0